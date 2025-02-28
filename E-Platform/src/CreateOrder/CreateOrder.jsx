import React, { useState, useEffect } from "react";
import "./CreateOrder.css"; // Ensure you have a CSS file for styling
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
            context_data.coupon_id = parseInt(e.target.value)
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

    const handleSubmit = (e) => {
        e.preventDefault();
        // Placeholder for API call to submit transaction
        alert("Order Placed Successfully!");
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
                const couponResponse = await axios.post(`${import.meta.env.VITE_API_URL}coupons/list`, {})

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
                        <option value=""> Continue without Coupons </option>
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
                        </>
                    )}

                    <button type="submit" disabled={!qrVisible || !transactionId}>Submit</button>
                </form>
            </div>
        </div>
    );
};

export default CreateOrder;
