from .consumers import ws_connect, ws_receive, ws_disconnect, launch

from channels import route

# The channel routing defines what channels get handled by what consumers,
# including optional matching on message attributes. In this example, we match
# on a path prefix, and then include routing from the chat module.
websocket_routing = [
    # Include sub-routing from an app.
    route("websocket.connect", ws_connect),

    # Called when WebSockets get sent a data frame
    route("websocket.receive", ws_receive),

    # Called when WebSockets disconnect
    route("websocket.disconnect", ws_disconnect),
]

timer_routing = [
    route("timer.start", launch)

]
