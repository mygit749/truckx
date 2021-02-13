 @app.route('/LOGIN', methods=['GET'])
    def LOGIN():
        data = request.form
        pusher.trigger(u'LOGIN',  {
            u'imei': data['12345678'],
        })
@app.route('/ALARM', methods=['POST'])
    def ALARM():
        data = request.form
        pusher.trigger(u'ALARM',  {
u'alarm_type': ['CRASH'],
u'alarm_time': ['2020-08-18 16:45:35'],
u'latitude': ['32.378903'],
u'longitude': ['-122.457324'],
u'file_list': ['a.mp4', 'b.mp4'],
        })        
@app.route('/LOCTION', methods=['GET'])
    def LOCTION():
        data = request.form
        pusher.trigger(u'LOCTION',  {
u'loction_time': ['2020-08-18 16:45:35'],
u'latitude': ['32.378903'],
u'longitude': ['-122.457324'],
        }) 
@app.route('/', methods=['POST'])
    def file():
  {
u'imei': data['12345678'],
u'filename': ['sample.mp4'],
u'data': ['video_data'],
        }) 
 
