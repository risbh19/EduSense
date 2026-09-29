const LearningPath = ({ skillGaps = [] }) => {
    if (!skillGaps.length) return null;

    return (
        <div className="section learning-path">
            <div className="section-title">
                Personalized Learning Path
            </div>

            <p className="path-intro">
                Based on your skill gaps, follow this learning sequence
                to strengthen your understanding step by step.
            </p>

            <div className="path-steps">

                <div className="path-step">
                    <div className="step-number">1</div>
                    <div className="step-content">
                        <h3>Understand the Basics</h3>
                        <p>
                            Start with the fundamental concepts of your
                            identified skill gaps.
                        </p>
                    </div>
                </div>

                <div className="path-line"></div>

                <div className="path-step">
                    <div className="step-number">2</div>
                    <div className="step-content">
                        <h3>Learn Through Videos</h3>
                        <p>
                            Watch the recommended video lectures to build
                            a clear conceptual understanding.
                        </p>
                    </div>
                </div>

                <div className="path-line"></div>

                <div className="path-step">
                    <div className="step-number">3</div>
                    <div className="step-content">
                        <h3>Read & Revise</h3>
                        <p>
                            Use the recommended articles to revise and
                            strengthen the concepts.
                        </p>
                    </div>
                </div>

                <div className="path-line"></div>

                <div className="path-step">
                    <div className="step-number">4</div>
                    <div className="step-content">
                        <h3>Practice Problems</h3>
                        <p>
                            Solve practice problems to test your
                            understanding and improve your skills.
                        </p>
                    </div>
                </div>

            </div>

            <div className="focus-skills">
                <span>Focus areas:</span>

                {skillGaps.map((skill) => (
                    <span
                        key={skill}
                        className="focus-skill"
                    >
                        {skill}
                    </span>
                ))}
            </div>
        </div>
    );
};

export default LearningPath;