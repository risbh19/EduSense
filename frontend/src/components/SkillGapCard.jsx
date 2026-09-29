const SkillGapCard = ({
    skillGaps = [],
    possibleGaps = [],
    strengths = [],
    gapSeverity
}) => {
    const hasAnything =
        skillGaps.length ||
        possibleGaps.length ||
        strengths.length;

    if (!hasAnything) return null;

    return (
        <div className="section skill-analysis">
            <div className="section-title">
                Skill Analysis
            </div>

            <div className="skill-grid">

                {/* Skill Gaps */}
                {skillGaps.length > 0 && (
                    <div className="skill-category gap-category">
                        <div className="category-header">
                            <span className="category-icon">⚠</span>
                            <div>
                                <h3>Skill Gaps</h3>
                                <p>Areas that need improvement</p>
                            </div>
                        </div>

                        <div className="skill-list">
                            {skillGaps.map((skill) => (
                                <span
                                    key={skill}
                                    className="skill-tag gap"
                                >
                                    {skill}
                                </span>
                            ))}
                        </div>
                    </div>
                )}

                {/* Possible Gaps */}
                {possibleGaps.length > 0 && (
                    <div className="skill-category possible-category">
                        <div className="category-header">
                            <span className="category-icon">~</span>
                            <div>
                                <h3>Possible Gaps</h3>
                                <p>Topics worth reviewing</p>
                            </div>
                        </div>

                        <div className="skill-list">
                            {possibleGaps.map((skill) => (
                                <span
                                    key={skill}
                                    className="skill-tag possible"
                                >
                                    {skill}
                                </span>
                            ))}
                        </div>
                    </div>
                )}

                {/* Strengths */}
                {strengths.length > 0 && (
                    <div className="skill-category strength-category">
                        <div className="category-header">
                            <span className="category-icon">✓</span>
                            <div>
                                <h3>Strengths</h3>
                                <p>Topics you seem comfortable with</p>
                            </div>
                        </div>

                        <div className="skill-list">
                            {strengths.map((skill) => (
                                <span
                                    key={skill}
                                    className="skill-tag strength"
                                >
                                    {skill}
                                </span>
                            ))}
                        </div>
                    </div>
                )}
            </div>

            {/* Severity */}
            {gapSeverity && (
                <div className="severity-row">
                    <span
                        className={`severity-dot ${gapSeverity}`}
                    />

                    <span>
                        Gap Severity:
                        <strong> {gapSeverity}</strong>
                    </span>
                </div>
            )}
        </div>
    );
};

export default SkillGapCard;