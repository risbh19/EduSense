const ResultCard = ({ sentiment }) => {
    if (!sentiment) return null;

    const label = sentiment.label?.toUpperCase() || "NEUTRAL";
    const confidence = Math.min(
        100,
        Math.max(0, sentiment.score * 100)
    ).toFixed(1);

    const sentimentConfig = {
        POSITIVE: {
            icon: "😊",
            title: "Positive Sentiment",
            description: "Your feedback shows a positive learning experience."
        },
        NEGATIVE: {
            icon: "🎯",
            title: "Learning Challenge Detected",
            description: "EduSense detected areas where additional support may help."
        },
        NEUTRAL: {
            icon: "💭",
            title: "Neutral Sentiment",
            description: "Your feedback reflects a balanced learning experience."
        }
    };

    const current =
        sentimentConfig[label] || sentimentConfig.NEUTRAL;

    return (
        <div className={`sentiment-card modern-sentiment ${label}`}>

            {/* Card Header */}
            <div className="sentiment-header">
                <div className="sentiment-heading-left">
                    <div className="sentiment-icon-box">
                        {current.icon}
                    </div>

                    <div>
                        <span className="sentiment-eyebrow">
                            AI SENTIMENT ANALYSIS
                        </span>

                        <h3>{current.title}</h3>
                    </div>
                </div>

                <span className={`badge sentiment-badge ${label}`}>
                    <span className="badge-dot"></span>
                    {label}
                </span>
            </div>

            {/* Main Content */}
            <div className="sentiment-body">

                <div className="confidence-panel">
                    <span className="confidence-label">
                        AI Confidence
                    </span>

                    <div className="confidence-number">
                        {confidence}
                        <span>%</span>
                    </div>

                    <span className="confidence-caption">
                        Prediction confidence
                    </span>
                </div>

                <div className="sentiment-details">

                    <p className="sentiment-description">
                        {current.description}
                    </p>

                    <div className="interpretation-box">
                        <span className="interpretation-icon">
                            ✦
                        </span>

                        <p>
                            {sentiment.interpretation}
                        </p>
                    </div>

                    <div className="confidence-progress-header">
                        <span>Confidence Score</span>
                        <strong>{confidence}%</strong>
                    </div>

                    <div className="confidence-bar modern-confidence-bar">
                        <div
                            className={`confidence-fill ${label}`}
                            style={{
                                width: `${confidence}%`
                            }}
                        />
                    </div>

                </div>
            </div>
        </div>
    );
};

export default ResultCard;