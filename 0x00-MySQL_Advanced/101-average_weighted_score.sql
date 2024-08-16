-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_weighted_score FLOAT;

    SELECT SUM(c.score * p.weight) INTO total_weighted_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id;

    SELECT SUM(weight) INTO total_weight
    FROM projects;

    SET avg_weighted_score = total_weighted_score / total_weight;

    UPDATE users
    SET average_score = avg_weighted_score;

    SELECT * FROM users;
END //
DELIMITER ;
