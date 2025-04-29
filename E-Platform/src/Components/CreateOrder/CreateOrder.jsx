import './CreateOrder.css';
import { SiEducative } from "react-icons/si";
import { useState, useEffect } from 'react';
import { toast } from 'react-toastify';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';



const CreateOrder = ({ isOpen, onClose, courseDetail }) => {

    const navigate = useNavigate();

    const [coupon, setCoupon] = useState('');
    const [discountAmount, setDiscountAmount] = useState(0);
    const [finalPrice, setFinalPrice] = useState(courseDetail.fees);
    const [couponId, setCouponId] = useState(null);
    const [isCouponApplied, setIsCouponApplied] = useState(false);
    

    const placeOrder = async () => {
        try {
            const response = await axios.post(
               `${import.meta.env.VITE_API_URL}orders/create_orders`,
               {
                    course_id: courseDetail.id,
                    coupon_id: couponId,
                    amount_payable: finalPrice
               },
               {
                    headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
               }
            )

            if (response.status == 201) {
                toast.success(response.data);
                console.log("checkout url:::", response.data.checkout_url)
                window.location.href = response.data.checkout_url;
            }
        } catch (error) {
            const message =
                error.response?.data?.message || 'Something went wrong while placing the order.';
            toast.error(message);
        }
    };

    const validateCoupon = async () => {
        try {
            const response = await axios.post(
                `${import.meta.env.VITE_API_URL}coupons/verify-coupon`,
                {
                    course_id: courseDetail.id,
                    coupon_code: coupon
                },
                {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`
                    }
                }
            );
    
            if (response.status === 200) {
                toast.success(response.data.message);
                if (response.data.verified) {
                    setDiscountAmount(response.data.discount_amount);
                    setFinalPrice(response.data.payable_amount);
                    setIsCouponApplied(true);
                    setCouponId(response.data.coupon_id);
                }
            } else {
                toast.error(response.data.message || 'Failed to apply coupon');
            }
        } catch (error) {
            const message =
                error.response?.data?.message || 'Something went wrong while applying the coupon.';
            toast.error(message);
        }
    };

    const removeCoupon = () => {
        setIsCouponApplied(false);
        setDiscountAmount(0);
        setFinalPrice(courseDetail.fees);
        setCoupon('');
        toast.info("Coupon removed");
    };

    if (!isOpen) return null;

    return (
        <div className="order-summary-container" onClick={onClose}>
            <div className="order-card" onClick={(e) => e.stopPropagation()}>
                <button className="close-button" onClick={onClose}>×</button>

                <div className="nav_header">
                    <div className="logo"><SiEducative/></div>
                    <h2 className="nav_logo"><span>Edu</span>Verse</h2>
                </div>

                <h2 className="course-title">{courseDetail.course_name}</h2>
                <p className="course-description">
                    {courseDetail.course_description}
                </p>

                <div className="order-detail">
                    <span className="order-label">Course Validity:</span>
                    <span className="order-value">{courseDetail.duration} Months</span>
                </div>

                <div className="order-detail">
                    <span className="order-label">Purchaser:</span>
                    <span className="order-value">{localStorage.getItem('user_email')}</span>
                </div>

                <div className="price-section">
                    <span className="price-label">Price:</span>
                    <span className="price-value">₹ {courseDetail.fees}</span>
                </div>

                <div className='price-section'>
                    <span className="price-label">Discount:</span>
                    <span className="price-value">₹ {discountAmount}</span>
                </div>

                <div className="coupon-section">
                    <input
                        type="text"
                        placeholder="Enter coupon code"
                        className="coupon-input"
                        value={coupon}
                        onChange={(e) => setCoupon(e.target.value)}
                        disabled={isCouponApplied}
                    />
                    {!isCouponApplied ? (
                        <button className="apply-button secondary" onClick={validateCoupon}>Apply</button>
                    ) : (
                        <button className="apply-button danger" onClick={removeCoupon}>×</button>
                    )}
                </div>

                <div className="final-price-section">
                    <span className="final-price-label">Final Price:</span>
                    <span className="final-price-value">₹ {finalPrice}</span>
                </div>

                <button className="checkout-button primary" onClick={placeOrder}>Proceed to Checkout</button>
            </div>
        </div>
    );
};

export default CreateOrder;
