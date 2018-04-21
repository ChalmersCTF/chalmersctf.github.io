"""
Chalmersctf Events plugin
====================================

This plugin generates three lists: current events, passed_events, all_events.
These can be used to display event information easily.

"""

from datetime import datetime
from pelican import signals, utils
from collections import namedtuple
import logging

log = logging.getLogger(__name__)

current_events = []
passed_events = []
all_events = []
Event = namedtuple("Event", "start end metadata")

def parse_tstamp(ev, field_name):
    """Parse a timestamp string in format "YYYY-MM-DD HH:MM"
    :returns: datetime
    """
    try:
        return datetime.strptime(ev[field_name], '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        log.error("Unable to parse the '%s' field in the event named '%s': %s" \
            % (field_name, ev['title'], e))
        raise

def parse_article(generator, metadata):
    """Collect articles metadata to be used for building the event calendar
    :returns: None
    """
    if 'Event-start' not in metadata and 'Event-end' not in metadata:
        return
    else:
        msg = "Both 'Event-start' and 'Event-end' must be" + \
            " speciefied in the event named '{}'".format(metadata['title'])
        log.error(msg)
        raise ValueError(msg)

    current_ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start = parse_tstamp(metadata, 'Event-start')
    end = parse_tstamp(metadata, 'Event-end')
    print(current_ts)
    if start > current_ts and end < current_ts:
        current_events.append(Event(dtstart, dtend, metadata))
    if end < current_ts:
        passed_events.append(Event(dtstart, dtend, metadata))
    all_events.append(Event(dtstart, dtend, metadata))

def generate_events_list(generator):
    """Populate the event_list variable to be used in jinja templates"""
    generator.context['current_events'] = sorted(current_events, reverse = True, key=lambda ev: (ev.start, ev.end))
    generator.context['passed_events'] = sorted(passed_events, reverse = True, key=lambda ev: (ev.start, ev.end))
    generator.context['all_events'] = sorted(all_events, reverse = True, key=lambda ev: (ev.start, ev.end))

def initialize_events(article_generator):
    """
    Clears the events list before generating articles to properly support plugins with
    multiple generation passes like i18n_subsites
    """
    current_events.clear()
    passed_events.clear()
    all_events.clear()

def register():
    signals.page_generator_init.connect(initialize_events)
    signals.page_generator_context.connect(parse_article)
    signals.page_generator_finalized.connect(generate_events_list)
