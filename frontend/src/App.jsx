import { useEffect, useState } from "react";
import axios from "axios";

import LearningPath from "./components/LearningPath";
import History from "./components/History";
import FeedbackInput from "./components/FeedbackInput";
import ResultCard from "./components/ResultCard";
import SkillGapCard from "./components/SkillGapCard";
import RecommendationList from "./components/RecommendationList";

const API = "http://localhost:8000";

export default function App() {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [result, setResult] = useState(null);

    const [activePage, setActivePage] = useState("dashboard");

    // =====================================================
    // LIGHT / DARK MODE
    // =====================================================

    const [darkMode, setDarkMode] = useState(() => {
        return localStorage.getItem("edusense-theme") === "dark";
    });

    useEffect(() => {
        document.body.classList.toggle("dark-mode", darkMode);

        localStorage.setItem(
            "edusense-theme",
            darkMode ? "dark" : "light"
        );
    }, [darkMode]);


    // =====================================================
    // DASHBOARD STATS
    // =====================================================

    const [stats, setStats] = useState({
        total_analyses: 0,
        total_skill_gaps: 0,
        unique_skills: 0,
        learning_paths: 0
    });

    const [progress, setProgress] = useState([]);
    const [progressLoading, setProgressLoading] = useState(false);


    // =====================================================
    // FETCH DASHBOARD / PROGRESS DATA
    // =====================================================

    useEffect(() => {
        const fetchData = async () => {
            try {
                // Dashboard statistics
                const statsResponse = await axios.get(
                    `${API}/stats`
                );

                setStats(statsResponse.data);

                // Learning progress
                if (activePage === "progress") {
                    setProgressLoading(true);

                    const progressResponse = await axios.get(
                        `${API}/progress`
                    );

                    setProgress(
                        progressResponse.data.progress || []
                    );
                }
            } catch (err) {
                console.error(
                    "Failed to fetch data:",
                    err
                );
            } finally {
                setProgressLoading(false);
            }
        };

        fetchData();
    }, [activePage]);


    // =====================================================
    // ANALYZE FEEDBACK
    // =====================================================

    const handleSubmit = async (text) => {
        setLoading(true);
        setError(null);
        setResult(null);

        try {
            const { data } = await axios.post(
                `${API}/analyze`,
                { text }
            );

            setResult(data);

            // Refresh dashboard statistics
            const statsResponse = await axios.get(
                `${API}/stats`
            );

            setStats(statsResponse.data);

            // Refresh progress
            if (activePage === "progress") {
                const progressResponse = await axios.get(
                    `${API}/progress`
                );

                setProgress(
                    progressResponse.data.progress || []
                );
            }

            setActivePage("dashboard");

        } catch (err) {
            setError(
                err.response?.data?.detail ||
                "Something went wrong. Is the backend running?"
            );
        } finally {
            setLoading(false);
        }
    };


    // =====================================================
    // NAVIGATION
    // =====================================================

    const navigateTo = (page) => {
        setActivePage(page);
        setError(null);
    };


    // =====================================================
    // MAIN UI
    // =====================================================

    return (
        <div className="app-shell">

            {/* =================================================
                SIDEBAR
            ================================================= */}

            <aside className="sidebar">

                <div className="brand">

                    <div className="brand-logo">
                        E
                    </div>

                    <div>
                        <h1>EduSense</h1>
                        <span>AI Learning Assistant</span>
                    </div>

                </div>


                <nav className="sidebar-nav">

                    <button
                        className={`nav-item ${
                            activePage === "dashboard"
                                ? "active"
                                : ""
                        }`}
                        onClick={() =>
                            navigateTo("dashboard")
                        }
                    >
                        <span>⌂</span>
                        Dashboard
                    </button>


                    <button
                        className={`nav-item ${
                            activePage === "analyze"
                                ? "active"
                                : ""
                        }`}
                        onClick={() =>
                            navigateTo("analyze")
                        }
                    >
                        <span>✦</span>
                        Analyze Feedback
                    </button>


                    <button
                        className={`nav-item ${
                            activePage === "progress"
                                ? "active"
                                : ""
                        }`}
                        onClick={() =>
                            navigateTo("progress")
                        }
                    >
                        <span>↗</span>
                        Learning Progress
                    </button>


                    <button
                        className={`nav-item ${
                            activePage === "history"
                                ? "active"
                                : ""
                        }`}
                        onClick={() =>
                            navigateTo("history")
                        }
                    >
                        <span>◷</span>
                        History
                    </button>

                </nav>


                <div className="sidebar-bottom">

                    <div className="ai-status">

                        <span className="status-dot"></span>

                        <div>
                            <strong>AI Engine</strong>

                            <small>
                                Ready to analyze
                            </small>
                        </div>

                    </div>

                </div>

            </aside>


            {/* =================================================
                MAIN CONTENT
            ================================================= */}

            <main className="main-content">


                {/* =================================================
                    TOP BAR
                ================================================= */}

                <header className="topbar">

                    <div className="mobile-brand">

                        <div className="brand-logo">
                            E
                        </div>

                        <strong>
                            EduSense
                        </strong>

                    </div>


                    <div className="topbar-right">

                        <div className="topbar-status">

                            <span className="status-dot"></span>

                            System Online

                        </div>


                        {/* LIGHT / DARK MODE BUTTON */}

                        <button
                            className="theme-toggle"
                            onClick={() =>
                                setDarkMode(!darkMode)
                            }
                            title={
                                darkMode
                                    ? "Switch to Light Mode"
                                    : "Switch to Dark Mode"
                            }
                            aria-label={
                                darkMode
                                    ? "Switch to Light Mode"
                                    : "Switch to Dark Mode"
                            }
                        >
                            {darkMode ? "☀️" : "🌙"}
                        </button>


                        <div className="profile">

                            <div className="profile-avatar">
                                S
                            </div>

                            <div className="profile-info">

                                <strong>
                                    Student
                                </strong>

                                <span>
                                    Learner
                                </span>

                            </div>

                        </div>

                    </div>

                </header>


                {/* =================================================
                    DASHBOARD
                ================================================= */}

                {activePage === "dashboard" && (

                    <div className="page">

                        {/* HERO */}

                        <section className="hero">

                            <div>

                                <span className="eyebrow">
                                    PERSONALIZED LEARNING
                                </span>

                                <h2>
                                    Learn smarter.
                                    <br />
                                    Improve faster. 🚀
                                </h2>

                                <p>
                                    Share your learning experience and
                                    let EduSense identify your skill gaps,
                                    analyze your sentiment, and recommend
                                    the right learning resources.
                                </p>

                            </div>

                        </section>


                        {/* STATISTICS */}

                        <section className="stats-grid">

                            <div className="stat-card">

                                <div className="stat-icon">
                                    🧠
                                </div>

                                <div>

                                    <span>
                                        AI Analyses
                                    </span>

                                    <strong>
                                        {stats.total_analyses}
                                    </strong>

                                </div>

                            </div>


                            <div className="stat-card">

                                <div className="stat-icon">
                                    🎯
                                </div>

                                <div>

                                    <span>
                                        Skill Gaps
                                    </span>

                                    <strong>
                                        {stats.total_skill_gaps}
                                    </strong>

                                </div>

                            </div>


                            <div className="stat-card">

                                <div className="stat-icon">
                                    📚
                                </div>

                                <div>

                                    <span>
                                        Skills Identified
                                    </span>

                                    <strong>
                                        {stats.unique_skills}
                                    </strong>

                                </div>

                            </div>


                            <div className="stat-card">

                                <div className="stat-icon">
                                    📈
                                </div>

                                <div>

                                    <span>
                                        Learning Paths
                                    </span>

                                    <strong>
                                        {stats.learning_paths}
                                    </strong>

                                </div>

                            </div>

                        </section>


                        {/* AI ANALYSIS */}

                        <section className="dashboard-card">

                            <div className="section-heading">

                                <div>

                                    <span className="section-kicker">
                                        AI ANALYSIS
                                    </span>

                                    <h3>
                                        How is your learning going?
                                    </h3>

                                    <p>
                                        Tell us what you understand,
                                        what you find difficult, or
                                        what you want to improve.
                                    </p>

                                </div>


                                <div className="heading-icon">
                                    ✦
                                </div>

                            </div>


                            <FeedbackInput
                                onSubmit={handleSubmit}
                                loading={loading}
                            />


                            {loading && (

                                <div className="loading">

                                    Analyzing your feedback

                                    <span className="loading-dot">
                                        ...
                                    </span>

                                </div>

                            )}


                            {error && (

                                <div className="error-box">
                                    ⚠ {error}
                                </div>

                            )}

                        </section>


                        {/* RESULTS */}

                        {result && (

                            <div className="analysis-results">

                                <ResultCard
                                    sentiment={
                                        result.sentiment
                                    }
                                />


                                <SkillGapCard
                                    skillGaps={
                                        result.skill_gaps
                                    }

                                    possibleGaps={
                                        result.possible_gaps
                                    }

                                    strengths={
                                        result.strengths
                                    }

                                    gapSeverity={
                                        result.gap_severity
                                    }
                                />


                                <LearningPath
                                    skillGaps={
                                        result.skill_gaps
                                    }
                                />


                                <RecommendationList
                                    recommendations={
                                        result.recommendations
                                    }

                                    strengthsFeedback={
                                        result.strengths_feedback
                                    }

                                    overallMessage={
                                        result.overall_message
                                    }
                                />

                            </div>

                        )}

                    </div>

                )}


                {/* =================================================
                    ANALYZE FEEDBACK
                ================================================= */}

                {activePage === "analyze" && (

                    <div className="page">

                        <div className="page-title">

                            <span className="section-kicker">
                                AI POWERED
                            </span>

                            <h2>
                                Analyze Your Feedback
                            </h2>

                            <p>
                                Get personalized insights into your
                                learning performance.
                            </p>

                        </div>


                        <div className="dashboard-card">

                            <FeedbackInput
                                onSubmit={handleSubmit}
                                loading={loading}
                            />


                            {loading && (

                                <div className="loading">

                                    Analyzing your feedback

                                    <span className="loading-dot">
                                        ...
                                    </span>

                                </div>

                            )}


                            {error && (

                                <div className="error-box">
                                    ⚠ {error}
                                </div>

                            )}

                        </div>


                        {result && (

                            <div className="analysis-results">

                                <ResultCard
                                    sentiment={
                                        result.sentiment
                                    }
                                />


                                <SkillGapCard
                                    skillGaps={
                                        result.skill_gaps
                                    }

                                    possibleGaps={
                                        result.possible_gaps
                                    }

                                    strengths={
                                        result.strengths
                                    }

                                    gapSeverity={
                                        result.gap_severity
                                    }
                                />


                                <LearningPath
                                    skillGaps={
                                        result.skill_gaps
                                    }
                                />


                                <RecommendationList
                                    recommendations={
                                        result.recommendations
                                    }

                                    strengthsFeedback={
                                        result.strengths_feedback
                                    }

                                    overallMessage={
                                        result.overall_message
                                    }
                                />

                            </div>

                        )}

                    </div>

                )}


                {/* =================================================
                    LEARNING PROGRESS
                ================================================= */}

                {activePage === "progress" && (

                    <div className="page">

                        <div className="page-title">

                            <span className="section-kicker">
                                YOUR JOURNEY
                            </span>

                            <h2>
                                Learning Progress
                            </h2>

                            <p>
                                Track your development and identify
                                areas that need more practice.
                            </p>

                        </div>


                        {/* LOADING */}

                        {progressLoading && (

                            <div className="dashboard-card empty-state">

                                <div className="empty-icon">
                                    ⏳
                                </div>

                                <h3>
                                    Loading Progress...
                                </h3>

                                <p>
                                    Fetching your learning progress
                                    from the database.
                                </p>

                            </div>

                        )}


                        {/* NO DATA */}

                        {!progressLoading &&
                            progress.length === 0 && (

                                <div className="dashboard-card empty-state">

                                    <div className="empty-icon">
                                        📈
                                    </div>

                                    <h3>
                                        No Progress Data Yet
                                    </h3>

                                    <p>
                                        Analyze some feedback to start
                                        building your personalized
                                        learning progress.
                                    </p>

                                </div>

                            )}


                        {/* PROGRESS CARDS */}

                        {!progressLoading &&
                            progress.length > 0 && (

                                <div className="progress-grid">

                                    {progress.map((item) => (

                                        <div
                                            className="progress-card"
                                            key={item.skill}
                                        >

                                            {/* CARD HEADER */}

                                            <div className="progress-card-header">

                                                <div>

                                                    <span className="progress-label">
                                                        SKILL
                                                    </span>

                                                    <h3>
                                                        {item.skill}
                                                    </h3>

                                                </div>


                                                <div className="progress-icon">
                                                    🎯
                                                </div>

                                            </div>


                                            {/* PROGRESS */}

                                            <div className="progress-main">

                                                <div>

                                                    <strong className="progress-percentage">
                                                        {
                                                            item.progress_percentage
                                                        }%
                                                    </strong>

                                                    <span>
                                                        Current Progress
                                                    </span>

                                                </div>


                                                <div
                                                    className={`progress-status-badge ${(
                                                        item.status || ""
                                                    )
                                                        .toLowerCase()
                                                        .replace(
                                                            /\s+/g,
                                                            "-"
                                                        )}`}
                                                >
                                                    {item.status}
                                                </div>

                                            </div>


                                            {/* PROGRESS BAR */}

                                            <div className="progress-bar">

                                                <div
                                                    className="progress-fill"
                                                    style={{
                                                        width: `${item.progress_percentage}%`
                                                    }}
                                                />

                                            </div>


                                            {/* ANALYSES */}

                                            <div className="progress-stat">

                                                <span>
                                                    Analyses
                                                </span>

                                                <strong>
                                                    {item.attempts}
                                                </strong>

                                            </div>


                                            {/* FIRST SEVERITY */}

                                            <div className="progress-stat">

                                                <span>
                                                    First Severity
                                                </span>

                                                <strong>
                                                    {
                                                        item.first_severity ||
                                                        "N/A"
                                                    }
                                                </strong>

                                            </div>


                                            {/* LATEST SEVERITY */}

                                            <div className="progress-stat">

                                                <span>
                                                    Latest Severity
                                                </span>

                                                <strong>
                                                    {
                                                        item.latest_severity ||
                                                        "N/A"
                                                    }
                                                </strong>

                                            </div>


                                            {/* IMPROVEMENT */}

                                            <div className="progress-stat">

                                                <span>
                                                    Improvement
                                                </span>

                                                <strong
                                                    className={
                                                        item.improvement > 0
                                                            ? "improvement-positive"
                                                            : item.improvement < 0
                                                                ? "improvement-negative"
                                                                : "improvement-neutral"
                                                    }
                                                >
                                                    {item.improvement > 0
                                                        ? `+${item.improvement}%`
                                                        : `${item.improvement}%`}
                                                </strong>

                                            </div>


                                            {/* SEVERITY HISTORY */}

                                            <div className="progress-history">

                                                <div className="history-title">
                                                    Severity History
                                                </div>

                                                <div className="history-items">

                                                    {(item.severity_history || [])
                                                        .map(
                                                            (
                                                                severity,
                                                                index
                                                            ) => (

                                                                <span
                                                                    className={`history-badge ${severity}`}
                                                                    key={`${severity}-${index}`}
                                                                >
                                                                    {severity}
                                                                </span>

                                                            )
                                                        )}

                                                </div>

                                            </div>


                                            {/* SENTIMENT HISTORY */}

                                            <div className="progress-history">

                                                <div className="history-title">
                                                    Sentiment History
                                                </div>

                                                <div className="history-items">

                                                    {(item.sentiment_history || [])
                                                        .map(
                                                            (
                                                                sentiment,
                                                                index
                                                            ) => (

                                                                <span
                                                                    className={`history-badge sentiment-${sentiment.toLowerCase()}`}
                                                                    key={`${sentiment}-${index}`}
                                                                >
                                                                    {sentiment}
                                                                </span>

                                                            )
                                                        )}

                                                </div>

                                            </div>


                                            {/* =================================================
                                                LEARNING TREND
                                            ================================================= */}

                                            <div className="learning-trend">

                                                <div className="trend-header">

                                                    <span>
                                                        Learning Trend
                                                    </span>

                                                    <strong>
                                                        {item.improvement > 0
                                                            ? `+${item.improvement}%`
                                                            : `${item.improvement}%`}
                                                    </strong>

                                                </div>


                                                <div className="trend-line">

                                                    {(item.severity_history || [])
                                                        .map(
                                                            (
                                                                severity,
                                                                index
                                                            ) => (

                                                                <div
                                                                    className="trend-point"
                                                                    key={`${severity}-${index}`}
                                                                >

                                                                    <div
                                                                        className={`trend-dot ${severity}`}
                                                                    ></div>

                                                                    <span>
                                                                        {index + 1}
                                                                    </span>

                                                                </div>

                                                            )
                                                        )}

                                                </div>


                                                <div className="trend-labels">

                                                    <span>
                                                        First Analysis
                                                    </span>

                                                    <span>
                                                        Latest Analysis
                                                    </span>

                                                </div>

                                            </div>

                                        </div>

                                    ))}

                                </div>

                            )}

                    </div>

                )}


                {/* =================================================
                    HISTORY
                ================================================= */}

                {activePage === "history" && (

                    <div className="page">

                        <div className="page-title">

                            <span className="section-kicker">
                                YOUR ACTIVITY
                            </span>

                            <h2>
                                Learning History
                            </h2>

                            <p>
                                Review your previous learning analyses.
                            </p>

                        </div>


                        <History />

                    </div>

                )}

            </main>

        </div>
    );
}