class Config:

    db_user = 'root'
    db_password = '1234'
    db_host = '172.17.0.2'
    database = 'pegacore'

    host = '0.0.0.0'
    port = 5112

    song_path = 'songs/'

    admin_name = 'admin'
    admin_pass = 'password'
    admin_enabled = True

    min_username_length = 4
    max_username_length = 16
    min_password_length = 6
    max_password_length = 64

    use_reverse_proxy = False

    do_audit_log = True
    log_path = ""