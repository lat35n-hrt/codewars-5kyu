def make_readable(seconds):

    t_hours = seconds // 3600
    t_minutes = (seconds % 3600) // 60
    t_seconds = (seconds % 3600) % 60

    t = "{}.zfill(2):{}.zfill(2):{}.zfill(2)".format(t_hours, t_minutes, t_seconds)

    return t



def make_readable(seconds):

    t_hours = seconds // 3600
    t_minutes = (seconds % 3600) // 60
    t_seconds = (seconds % 3600) % 60

    return str(t_hours).zfill(2)+':'+str(t_minutes).zfill(2)+':'+str(t_seconds).zfill(2)


# The first solution
# def make_readable(seconds):

#     t_hours = seconds // 3600
#     t_minutes = (seconds % 3600) // 60
#     t_seconds = (seconds % 3600) % 60
    
#     if t_hours < 10:
#         r_hours = str(0) + str(t_hours)
#     else:
#         r_hours = str(t_hours)

#     if t_minutes < 10:
#         r_minutes = str(0) + str(t_minutes)
#     else:
#         r_minutes = str(t_minutes)

#     if t_seconds < 10:
#         r_seconds = str(0) + str(t_seconds)
#     else:
#         r_seconds = str(t_seconds)

#     return r_hours+':'+r_minutes+':'+r_seconds

# TEST
# test.assert_equals(make_readable(0), "00:00:00")
# test.assert_equals(make_readable(5), "00:00:05")
# test.assert_equals(make_readable(60), "00:01:00")
# test.assert_equals(make_readable(86399), "23:59:59")
# test.assert_equals(make_readable(359999), "99:59:59")

# Research after submit
# t = "{:02d}:{:02d}:{:02d}".format(t_hours, t_minutes, t_seconds)