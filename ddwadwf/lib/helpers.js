/**
 *
 * @param {Response} res Express app response parameter
 * @param {Array} data Data to return as json to the endpoint
 * @param {string} message Message to return as json to the endpoint. Default: "success"
 * @param {number} status HTTP Status Code to return to endpoint. Default: 200
 * @returns
 */
function SuccessResponse(res, data = [], message = 'success', status = 200) {
	return res.json({ message, status, data })
}

/**
 *
 * @param {Response} res Express app response parameter
 * @param {Array} data Data to return as json to the endpoint
 * @param {string} message Message to return as json to the endpoint. Default: "error"
 * @param {number} status HTTP Status Code to return to endpoint. Default: 500
 * @returns
 */
function ErrorResponse(res, data = [], message = 'error', status = 500) {
	return res.json({ message, status, data })
}

module.exports = { SuccessResponse, ErrorResponse }
