drop table FraudMetrixEventDecode

CREATE TABLE FraudMetrixEventDecode (
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	UserId bigint NOT NULL,
	EventType nvarchar(50) NOT NULL,
	RefId bigint NOT NULL,
	Status int NOT NULL,
	Decision nvarchar(50),
	Score int,
	f_score int,
	f_decision nvarchar(32),
	evt_hitrules tinyint,
	--异常借款--
	evt_use_http tinyint,
	evt_use_socket tinyint,
	evt_use_vpn tinyint,
	evt_device_less_err tinyint,
	evt_cell_loan_bdaw tinyint,
	evt_cell_addr_err tinyint,
	evt_ip_err tinyint,
	evt_shortterm_login_loan tinyint,
	evt_shortterm_loans tinyint,
	evt_cell_loans_tmonth tinyint,
	evt_id_loans_tmonth tinyint,
	evt_email_loans_tmonth tinyint,
	evt_phone_loans_tmonth tinyint,
	evt_device_loans_tmonth tinyint,
	evt_home_loans_tmonth tinyint,
	evt_loans_oday tinyint,
	evt_accounts_loan_oday tinyint,
	evt_accounts_loan_sday tinyint,
	evt_ips_loan_oday tinyint,
	evt_ips_loan_sday tinyint,
	evt_devices_loan_oday tinyint,
	evt_devices_loan_sday tinyint,
	evt_android_simulater tinyint,
	--机构代办--
	evt_device_accounts_oday tinyint,
	evt_device_accounts_sday tinyint,
	evt_device_sub_info_oday tinyint,
	evt_device_sub_info_sday tinyint,
	--失信借款--
	evt_cell_blacks tinyint,
	evt_cell_virtual tinyint,
	evt_cell_short_number tinyint,
	evt_id_blacks tinyint,
	evt_device_blacks tinyint,
	evt_ip_blacks tinyint,
	evt_contact_blacks tinyint,
	evt_addr_blacks tinyint,
	evt_id_court_blacks tinyint,
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL
);

CREATE INDEX FraudMetrixEventDecode ON FraudMetrixEventDecode (ID);

CREATE TABLE FraudHitrulesConfig (
	id int NOT NULL,
	colname nvarchar(50) NOT NULL,
	notes  nvarchar(50) NOT NULL,
);
drop table FraudHitrulesConfig

SELECT id, colname, notes FROM FraudHitrulesConfig;

delete from FraudHitrulesConfig

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51450, 'evt_use_http', '实用HTTP代理进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51520, 'evt_use_http', '实用HTTP代理进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51452, 'evt_use_socket', '实用SOCKET4_5代理进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51522, 'evt_use_socket', '实用SOCKET4_5代理进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51454, 'evt_use_vpn', '实用VPN代理进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51524, 'evt_use_vpn', '实用VPN代理进行借款');

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51456, 'evt_device_less_err', '借款时设备标示缺失异常');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51526, 'evt_device_less_err', '借款时设备标示缺失异常');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51458, 'evt_cell_loan_bdaw', '在1点到5点进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51528, 'evt_cell_loan_bdaw', '在1点到5点进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51460, 'evt_cell_addr_err', '不在手机归属地借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51530, 'evt_cell_addr_err', '不在手机归属地借款');

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51462, 'evt_ip_err', '借款IP与真实IP的城市不匹配');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51532, 'evt_ip_err', '借款IP与真实IP的城市不匹配');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (52464, 'evt_shortterm_login_loan', '设备或账户登录和借款的时间间隔极短');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51534, 'evt_shortterm_login_loan', '设备或账户登录和借款的时间间隔极短');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (52466, 'evt_shortterm_loans', '账户或设备两次借款时间间隔极短');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51536, 'evt_shortterm_loans', '账户或设备两次借款时间间隔极短');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51468, 'evt_cell_loans_tmonth', '3个月内手机在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51538, 'evt_cell_loans_tmonth', '3个月内手机在多个平台进行借款');

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51470, 'evt_id_loans_tmonth', '3个月内身份证在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51540, 'evt_id_loans_tmonth', '3个月内身份证在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51472, 'evt_email_loans_tmonth', '3个月内邮箱在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51542, 'evt_email_loans_tmonth', '3个月内邮箱在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51474, 'evt_phone_loans_tmonth', '3个月内座机在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51544, 'evt_phone_loans_tmonth', '3个月内座机在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51476, 'evt_device_loans_tmonth', '3个月内设备在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51546, 'evt_device_loans_tmonth', '3个月内设备在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51478, 'evt_home_loans_tmonth', '3个月内借款人家庭住址在多个平台进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51548, 'evt_home_loans_tmonth', '3个月内在多个平台进行借款');

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51480, 'evt_loans_oday', '1天内设备或账户借款次数过多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51550, 'evt_loans_oday', '1天内设备或账户借款次数过多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51482, 'evt_accounts_loan_oday', '1天内设备使用过多账户进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51552, 'evt_accounts_loan_oday', '1天内设备使用过多账户进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51484, 'evt_accounts_loan_sday', '7天内设备使用过多账户进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51554, 'evt_accounts_loan_sday', '7天内设备使用过多账户进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51486, 'evt_ips_loan_oday', '1天内设备使用过多IP进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51556, 'evt_ips_loan_oday', '1天内设备使用过多IP进行借款');

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51488, 'evt_ips_loan_sday', '7天内设备使用过多IP进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51558, 'evt_ips_loan_sday', '7天内设备使用过多IP进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51490, 'evt_devices_loan_oday', '1天内账户在过多的设备上进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51560, 'evt_devices_loan_oday', '1天内账户在过多的设备上进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51492, 'evt_devices_loan_sday', '7天内账户在过多的设备上进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51562, 'evt_devices_loan_sday', '7天内账户在过多的设备上进行借款');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51842, 'evt_android_simulater', '使用android模拟器借款');

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51494, 'evt_device_accounts_oday', '1天内设备上进行借款的账户极多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51564, 'evt_device_accounts_oday', '1天内设备上进行借款的账户极多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51496, 'evt_device_accounts_sday', '7天内设备上进行借款的账户极多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51566, 'evt_device_accounts_sday', '7天内设备上进行借款的账户极多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51498, 'evt_device_sub_info_oday', '1天内设备上提交的个人信息极多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51568, 'evt_device_sub_info_oday', '1天内设备上提交的个人信息极多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51500, 'evt_device_sub_info_sday', '7天内设备上提交的个人信息极多');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51570, 'evt_device_sub_info_sday', '7天内设备上提交的个人信息极多');

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51432, 'evt_cell_blacks', '借款手机号命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51502, 'evt_cell_blacks', '借款手机号命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51434, 'evt_cell_virtual', '借款手机号命中虚假手机号码证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51504, 'evt_cell_virtual', '借款手机号命中虚假手机号码证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51436, 'evt_cell_short_number', '借款手机号命中通信小号证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51506, 'evt_cell_short_number', '借款手机号命中通信小号证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51438, 'evt_id_blacks', '借款身份证号命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51508, 'evt_id_blacks', '借款身份证号命中全局失信证据库');

INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51440, 'evt_device_blacks', '借款时设备命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51510, 'evt_device_blacks', '借款时设备命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51442, 'evt_ip_blacks', '借款时IP命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51512, 'evt_ip_blacks', '借款时IP命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51444, 'evt_contact_blacks', '常用联系人手机命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51514, 'evt_contact_blacks', '常用联系人手机命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51446, 'evt_addr_blacks', '借款人地址命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51516, 'evt_addr_blacks', '借款人地址命中全局失信证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51448, 'evt_id_court_blacks', '借款人身份证命中法院执行证据库');
INSERT INTO FraudHitrulesConfig
(id, colname, notes) VALUES (51518, 'evt_id_court_blacks', '借款人身份证命中法院执行证据库');



