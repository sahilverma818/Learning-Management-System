import React, { useState, useEffect } from "react";
import "./CreateOrder.css";
import { useParams } from "react-router-dom";
import { toast } from "react-toastify";
import axios from "axios";

const CreateOrder = ({ isOpen, onClose }) => {

    const {id} = useParams();
    const [couponId, setCouponId] = useState("");
    const [isCouponValid, setIsCouponValid] = useState();
    const [transactionId, setTransactionId] = useState("");
    const [qrVisible, setQrVisible] = useState(false);
    const [couponData, setCouponData] = useState([])
    const [paymentData, setPaymentData] = useState({})

    const handleCouponValidation = async (e) => {

        setCouponId(e.target.value)
        const context_data = {
            "course_id": parseInt(id),
        }
        if (e.target.value != "") {
            let coupon_id = parseInt(e.target.value)
            if (coupon_id != "0") {
                context_data.coupon_id = parseInt(coupon_id)
            }
        }
        try {
            const validateCoupon = await axios.post(`${import.meta.env.VITE_API_URL}orders/generate-qr`, context_data)

            if (validateCoupon.status === 200){
                setIsCouponValid(true)
                setQrVisible(true)
                setPaymentData(validateCoupon.data)
            }
        } catch (error) {
            setIsCouponValid(false);
            setQrVisible(false);
            toast.error(error.response?.data?.message || "An error occurred");
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            const orderCreate = await axios.post(`${import.meta.env.VITE_API_URL}orders/create_orders`, {
                "course_id": couponId,
                "course_id": parseInt(id),
                "amount_payable": paymentData.amount_payable,
                "payment_method": "UPI",
                "transaction_id": transactionId
            }, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    'accept': 'application/json'
                }
            })

            if (orderCreate.status == 200) {
                toast.success('Order Placed Successfully. You will get further update on registered mail')
            }
        } catch(error) {
            toast.error('Failed to Create Order. Try again or contact support.')
        }
        onClose();
    };

    const handleClose = () => {
        setIsCouponValid(false);
        setQrVisible(false);
        onClose();
    }

    useEffect(() => {
        const fetchCoupons = async () => {
            try {
                const couponResponse = await axios.post(`${import.meta.env.VITE_API_URL}coupons/get_coupons`, {})

                if (couponResponse.status === 200) {
                    setCouponData(couponResponse.data)
                }
            } catch (error) {
                toast.error(error.response?.data?.message || "An error occurred");
            }
        }
        fetchCoupons();
    }, [])

    if (paymentData) {
        console.log(paymentData);
        
    }
    if (!isOpen) return null;

    return (
        <div className="popup-order-overlay">
            <div className="popup-order-container">
                <button className="close-order-btn" onClick={handleClose}>&times;</button>
                <h2>Place Order</h2>
                <form onSubmit={handleSubmit}>
                    <label>Coupon ID:</label>
                    <select id="coupon_id" name="coupon_id" onChange={handleCouponValidation} value={couponId} required>
                        <option value="" disabled>-- Select a Coupon --</option>
                        <option value="0"> Continue without Coupons </option>
                        { couponData && (
                        couponData.map((coupon) => (
                            <option key={coupon.id} value={coupon.id}> { coupon.code } </option>
                        ))
                    )}
                    </select>
                    {isCouponValid === false && <p className="error-order">Invalid Coupon</p>}

                    <label>Amount Payable:</label>
                    <input type="text" value={paymentData.amount_payable} disabled />

                    <label>Payment Method:</label>
                    <input type="text" value="UPI" disabled />

                    <label>QR Code:</label>
                    <div className={`qr-order-code ${qrVisible ? "clear-order" : "blurry-order"}`}>
                        <img
                            src={`${import.meta.env.VITE_API_URL}${paymentData.file_path}`}
                            alt="QR Code"
                            className={qrVisible ? "clear-order" : "blurry-order"}
                        />
                    </div>

                    {qrVisible && (
                        <>
                            <label>Transaction ID:</label>
                            <input
                                type="text"
                                value={transactionId}
                                onChange={(e) => setTransactionId(e.target.value)}
                                required
                            />
                            {console.log("????",transactionId)}
                        </>
                    )}

                    <button type="submit" disabled={(!qrVisible) && (transactionId == null)}>Submit</button>
                </form>
            </div>
        </div>
    );
};

export default CreateOrder;
