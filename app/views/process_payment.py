from flask import request, Blueprint, jsonify, make_response
import json

from app.payment.payment_service import Card
from app.payment.external_payment_services import ExternalPaymentService

pp_blueprint = Blueprint("process_payment", __name__)


@pp_blueprint.route("/ProcessPayment", methods=['POST'])
def process_payment():
    data = request.get_data(as_text=True)

    if not data:
        msg = "There is no data in the request"
        return make_response(jsonify({"status_code": 400, "msg": msg}), 400)
    json_data = json.loads(data)

    card_data = Card()
    try:
        status, msg = card_data.verify_input(**json_data)
        if not status:
            return make_response(jsonify({"status_code": 400, "msg": msg}), 400)

        payment_status = ExternalPaymentService(card_data.Amount, card_data)

        status, msg = payment_status.make_payment()
        if status:
            return make_response(jsonify({"status_code": 200, "msg": msg}), 200)
        else:
            return make_response(jsonify({"status_code": 400, "msg": msg}), 400)

    except:
        return make_response(jsonify({"status_code": 500, "msg": "whoops! something went wrong"}), 500)
