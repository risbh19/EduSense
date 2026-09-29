import { useEffect, useState } from "react";
import axios from "axios";

const API = "http://localhost:8000";

const History = () => {
    const [history, setHistory] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [expandedId, setExpandedId] = useState(null);

    useEffect(() => {
        const fetchHistory = async () => {
            try {
                const { data } = await axios.get(`${API}/history`);
                setHistory(data.history || []);
            } catch (error) {
                console.error("Failed to fetch history:", error);

                setError(
                    "Unable to load learning history. Please make sure the backend is running."
                );
            } finally {
                setLoading(false);
            }
        };

        fetchHistory();
    }, []);

    const toggleDetails = (id) => {
        setExpandedId(
            expandedId === id ? null : id
        );
    };

    const formatList = (value) => {
        if (!value) return [];

        return value
            .split(",")
            .map((item) => item.trim())
            .filter(Boolean);
    };

    if (loading) {
        return (
            <div className="section history-section">
                <div className="section-title">
                    Learning History
                </div>

                <div className="history-empty">
                    <div className="history-loading-icon">
                        ⏳
                    </div>

                    <h3>Loading your history...</h3>

                    <p>
                        Fetching your previous learning analyses.
                    </p>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="section history-section">
                <div className="section-title">
                    Learning History
                </div>

                <div className="history-error">
                    <span>⚠️</span>
                    <p>{error}</p>
                </div>
            </div>
        );
    }

    if (!history.length) {
        return (
            <div className="section history-section">
                <div className="section-title">
                    Learning History
                </div>

                <div className="history-empty">
                    <div className="history-empty-icon">
                        📊
                    </div>

                    <h3>No History Yet</h3>

                    <p>
                        Analyze some feedback to start building
                        your personalized learning history.
                    </p>
                </div>
            </div>
        );
    }

    return (
        <div className="section history-section">

            {/* Page Header */}
            <div className="history-page-header">
                <div>
                    <div className="section-title">
                        Learning History
                    </div>

                    <p className="history-subtitle">
                        Review your previous feedback analyses
                        and track your learning journey.
                    </p>
                </div>

                <div className="history-count">
                    {history.length}{" "}
                    {history.length === 1
                        ? "Analysis"
                        : "Analyses"}
                </div>
            </div>

            {/* History List */}
            <div className="history-list">

                {history.map((item) => {

                    const confidence =
                        item.sentiment_confidence
                            ? `${(
                                  item.sentiment_confidence * 100
                              ).toFixed(1)}%`
                            : "N/A";

                    const formattedDate =
                        item.created_at
                            ? new Date(
                                  item.created_at
                              ).toLocaleString()
                            : "N/A";

                    const topics =
                        formatList(item.topics);

                    const skillGaps =
                        formatList(item.skill_gaps);

                    const possibleGaps =
                        formatList(item.possible_gaps);

                    const strengths =
                        formatList(item.strengths);

                    const isExpanded =
                        expandedId === item.id;

                    return (
                        <div
                            className={`history-card ${
                                isExpanded
                                    ? "expanded"
                                    : ""
                            }`}
                            key={item.id}
                        >

                            {/* Card Header */}
                            <div className="history-header">

                                <div className="history-title">

                                    <span className="history-icon">
                                        🧠
                                    </span>

                                    <div>
                                        <span className="history-label">
                                            Learning Analysis
                                        </span>

                                        <h3>
                                            Analysis #{item.id}
                                        </h3>
                                    </div>

                                </div>

                                <span
                                    className={`badge ${
                                        item.sentiment
                                            ? item.sentiment.toUpperCase()
                                            : "NEUTRAL"
                                    }`}
                                >
                                    {item.sentiment || "N/A"}
                                </span>

                            </div>

                            {/* Feedback */}
                            <div className="history-feedback-box">

                                <span className="feedback-label">
                                    Your Feedback
                                </span>

                                <p className="history-feedback">
                                    "{item.feedback}"
                                </p>

                            </div>

                            {/* Basic Details */}
                            <div className="history-details">

                                <div className="history-detail">
                                    <span className="detail-label">
                                        🎯 Skill Gaps
                                    </span>

                                    <span className="detail-value">
                                        {item.skill_gaps ||
                                            "None"}
                                    </span>
                                </div>

                                <div className="history-detail">
                                    <span className="detail-label">
                                        ⚠ Severity
                                    </span>

                                    <span className="detail-value">
                                        {item.gap_severity
                                            ? item.gap_severity
                                                  .charAt(0)
                                                  .toUpperCase() +
                                              item.gap_severity.slice(1)
                                            : "N/A"}
                                    </span>
                                </div>

                                <div className="history-detail">
                                    <span className="detail-label">
                                        📊 Confidence
                                    </span>

                                    <span className="detail-value">
                                        {confidence}
                                    </span>
                                </div>

                                <div className="history-detail">
                                    <span className="detail-label">
                                        🕒 Date
                                    </span>

                                    <span className="detail-value">
                                        {formattedDate}
                                    </span>
                                </div>

                            </div>

                            {/* View Details Button */}
                            <button
                                className="history-details-btn"
                                onClick={() =>
                                    toggleDetails(item.id)
                                }
                            >
                                {isExpanded
                                    ? "Hide Details ↑"
                                    : "View Details →"}
                            </button>

                            {/* Expanded Details */}
                            {isExpanded && (
                                <div className="history-expanded">

                                    {/* Topics */}
                                    <div className="expanded-block">
                                        <h4>
                                            📚 Topics Identified
                                        </h4>

                                        {topics.length > 0 ? (
                                            <div className="history-tags">
                                                {topics.map(
                                                    (topic, index) => (
                                                        <span
                                                            className="history-tag"
                                                            key={index}
                                                        >
                                                            {topic}
                                                        </span>
                                                    )
                                                )}
                                            </div>
                                        ) : (
                                            <p>
                                                No topics recorded.
                                            </p>
                                        )}
                                    </div>

                                    {/* Skill Gaps */}
                                    <div className="expanded-block">
                                        <h4>
                                            ⚠ Skill Gaps
                                        </h4>

                                        {skillGaps.length > 0 ? (
                                            <div className="history-tags gap-tags">
                                                {skillGaps.map(
                                                    (skill, index) => (
                                                        <span
                                                            className="history-tag gap"
                                                            key={index}
                                                        >
                                                            {skill}
                                                        </span>
                                                    )
                                                )}
                                            </div>
                                        ) : (
                                            <p>
                                                No confirmed skill gaps.
                                            </p>
                                        )}
                                    </div>

                                    {/* Possible Gaps */}
                                    <div className="expanded-block">
                                        <h4>
                                            🔍 Possible Gaps
                                        </h4>

                                        {possibleGaps.length > 0 ? (
                                            <div className="history-tags">
                                                {possibleGaps.map(
                                                    (skill, index) => (
                                                        <span
                                                            className="history-tag possible"
                                                            key={index}
                                                        >
                                                            {skill}
                                                        </span>
                                                    )
                                                )}
                                            </div>
                                        ) : (
                                            <p>
                                                No possible gaps recorded.
                                            </p>
                                        )}
                                    </div>

                                    {/* Strengths */}
                                    <div className="expanded-block">
                                        <h4>
                                            ✓ Strengths
                                        </h4>

                                        {strengths.length > 0 ? (
                                            <div className="history-tags">
                                                {strengths.map(
                                                    (skill, index) => (
                                                        <span
                                                            className="history-tag strength"
                                                            key={index}
                                                        >
                                                            {skill}
                                                        </span>
                                                    )
                                                )}
                                            </div>
                                        ) : (
                                            <p>
                                                No strengths recorded.
                                            </p>
                                        )}
                                    </div>

                                    {/* Learning Summary */}
                                    {item.overall_message && (
                                        <div className="history-summary">

                                            <span className="summary-icon">
                                                💡
                                            </span>

                                            <div>
                                                <strong>
                                                    Learning Summary
                                                </strong>

                                                <p>
                                                    {item.overall_message}
                                                </p>
                                            </div>

                                        </div>
                                    )}

                                </div>
                            )}

                        </div>
                    );
                })}

            </div>
        </div>
    );
};

export default History;