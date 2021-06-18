import uuid

from models.event import EventStage

from utils.validate import validate_json
from utils.db import session
from utils.monitor import check_row_count_match


if __name__ == "__main__":
    source_file = 'sample_data.json'  # TODO: read as param
    line_count = {'valid': 0, 'invalid': 0}

    with open(f'sources/{source_file}', 'r') as f:
        for line in f:
            if validate_json(line)[0]:
                line_count['valid'] += 1
                json_data = validate_json(line)[1]

                event = EventStage(
                    uuid=str(uuid.uuid4()),
                    event_type=json_data['event_type'],
                    event_time=json_data['event_time'],
                    user_email=json_data['data']['user_email'],
                    phone_number=json_data['data']['phone_number'],
                    processing_date=json_data['processing_date'],
                )

                session.add(event)
                session.commit()

            else:
                line_count['invalid'] += 1
                print('Bad row:', line, validate_json(line)[1])

    if check_row_count_match('event_stage', line_count['valid']):
        session.execute('INSERT INTO event (SELECT * FROM event_stage)')
