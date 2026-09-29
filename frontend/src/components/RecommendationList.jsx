const RecommendationList = ({
    recommendations,
    strengthsFeedback,
    overallMessage
}) => {
    const allRecs = [
        ...(recommendations || []),
        ...(strengthsFeedback || [])
    ];

    if (!allRecs.length) return null;

    return (
        <div>
            {overallMessage && (
                <div className="overall-msg">
                    <span className="overall-icon">💡</span>
                    <div>
                        <strong>Your Learning Summary</strong>
                        <p>{overallMessage}</p>
                    </div>
                </div>
            )}

            <div className="section">
                <div className="section-title">
                    Recommended Resources
                </div>

                <div className="recommendation-list">
                    {allRecs.map((rec, i) => {
                        const isStrength =
                            rec.gap_type === "strength";

                        return (
                            <div
                                key={i}
                                className={`rec-item ${
                                    isStrength ? "strength-rec" : ""
                                }`}
                            >
                                <div className="rec-header">
                                    <div className="rec-skill-name">
                                        <span className="rec-arrow">
                                            {isStrength ? "✓" : "→"}
                                        </span>

                                        <span>{rec.skill}</span>
                                    </div>

                                    <span className="difficulty">
                                        {rec.difficulty}
                                    </span>
                                </div>

                                <div className="rec-message">
                                    {rec.message}
                                </div>

                                <div className="resources">
                                    {rec.resources.map((r, j) => (
                                        <a
                                            key={j}
                                            href={r.url}
                                            target="_blank"
                                            rel="noreferrer"
                                            className="resource-link"
                                        >
                                            <span
                                                className={`resource-type ${
                                                    r.type?.toLowerCase()
                                                }`}
                                            >
                                                {r.type === "video"
                                                    ? "▶ VIDEO"
                                                    : "📄 ARTICLE"}
                                            </span>

                                            <span className="resource-title">
                                                {r.title}
                                            </span>

                                            <span className="resource-arrow">
                                                ↗
                                            </span>
                                        </a>
                                    ))}
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};

export default RecommendationList;