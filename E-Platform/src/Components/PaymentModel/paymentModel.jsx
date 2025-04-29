import './paymentModel.css';
// import { SiCheckmarkCircle } from "react-icons/si";
import { IoClose } from "react-icons/io5";

const PaymentSuccessModal = ({ isOpen, onClose, paymentData }) => {
    if (!isOpen || !paymentData) return null;

    return (
        <div className="success-modal-overlay" onClick={onClose}>
            <div className="success-modal-card" onClick={(e) => e.stopPropagation()}>
                <button className="close-button" onClick={onClose}><IoClose /></button>
                <div className="success-icon">
                    {/* <SiCheckmarkCircle size={48} color="#4BB543" /> */} SUCCESS !!
                </div>
                <h2>Payment Successful!</h2>
                <p>Your transaction was completed successfully.</p>

                <div className="payment-details">
                    <div><strong>Order ID:</strong> {paymentData.order_id}</div>
                    <div><strong>Course ID:</strong> {paymentData.course_id}</div>
                    <div><strong>Total Amount:</strong> ₹ {paymentData.total_amount}</div>
                    <div><strong>Payment Status:</strong> {paymentData.payment_status}</div>
                    <div><strong>Session Status:</strong> {paymentData.session_status}</div>
                    <div><strong>Transaction ID:</strong> {paymentData.transaction_id}</div>
                    <div><strong>Indent ID:</strong> {paymentData.indent_id}</div>
                    <div><strong>Created At:</strong> {new Date(paymentData.created_at).toLocaleString()}</div>
                </div>

                <button className="go-back-button" onClick={onClose}>Close</button>
            </div>
        </div>
    );
};

export default PaymentSuccessModal;
