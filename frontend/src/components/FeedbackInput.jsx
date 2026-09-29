import { useState } from "react";

const FeedbackInput = ({ onSubmit, loading }) => {
    const [text, setText] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        const trimmedText = text.trim();

        if (trimmedText && !loading) {
            onSubmit(trimmedText);
        }
    };

    const remaining = 500 - text.length;

    return (
        <div className="input-card modern-feedback-card">

            {/* Header */}
            <div className="input-header">
                <div>
                    <label htmlFor="feedback">
                        Your Feedback
                    </label>

                    <p className="input-helper">
                        Share what you understand, what you're struggling
                        with, or what you want to improve.
                    </p>
                </div>

                <span
                    className={`counter ${
                        remaining < 50 ? "counter-warning" : ""
                    }`}
                >
                    {text.length}/500
                </span>
            </div>

            {/* Form */}
            <form onSubmit={handleSubmit}>

                <div className="textarea-wrapper">

                    <textarea
                        id="feedback"
                        name="feedback"
                        value={text}
                        maxLength={500}
                        onChange={(e) => setText(e.target.value)}
                        placeholder="For example: I'm struggling to understand recursion and dynamic programming..."
                        disabled={loading}
                        rows={6}
                    />

                    {!text && !loading && (
                        <div className="textarea-hint">
                            💡 Tip: Mention a specific topic or concept for
                            more relevant recommendations.
                        </div>
                    )}

                </div>

                {/* Action area */}
                <div className="input-footer">

                    <span className="input-status">
                        {loading ? (
                            <>
                                <span className="status-dot analyzing"></span>
                                AI is analyzing your feedback...
                            </>
                        ) : (
                            <>
                                <span className="status-dot ready"></span>
                                Ready for analysis
                            </>
                        )}
                    </span>

                    <button
                        className="submit-btn"
                        type="submit"
                        disabled={loading || !text.trim()}
                    >
                        {loading ? (
                            <>
                                <span className="spinner"></span>
                                Analyzing...
                            </>
                        ) : (
                            <>
                                Analyze My Feedback
                                <span className="button-arrow">→</span>
                            </>
                        )}
                    </button>

                </div>

            </form>
        </div>
    );
};

export default FeedbackInput;