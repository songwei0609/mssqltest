
drop table BfdMatchDataV2Decode

CREATE TABLE BfdMatchDataV2Decode (
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	CitizenNo nvarchar(50) NOT NULL,
	Mobilephone nvarchar(50) NOT NULL,
	ApiFlag int NOT NULL DEFAULT ((0)),
	BfdAudit int NOT NULL DEFAULT ((0)),
	FailedStatus int NOT NULL DEFAULT ((-1)),
	code nvarchar(50) NOT NULL,
	swift_number nvarchar(50),
	--Flag--
	f_accountchange tinyint NOT NULL DEFAULT ((0)),
 	f_applyLoan tinyint NOT NULL DEFAULT ((0)),
	f_assets tinyint NOT NULL DEFAULT ((0)),
	f_brand tinyint NOT NULL DEFAULT ((0)),
	f_consumption tinyint NOT NULL DEFAULT ((0)),
	f_location tinyint NOT NULL DEFAULT ((0)),
	f_media tinyint NOT NULL DEFAULT ((0)),
	f_ruleapplyloan tinyint NOT NULL DEFAULT ((0)),
	f_ruleloan_android tinyint NOT NULL DEFAULT ((0)),
	f_ruleloan_ios tinyint NOT NULL DEFAULT ((0)),
	f_rulespeciallist tinyint NOT NULL DEFAULT ((0)),
	f_score tinyint NOT NULL DEFAULT ((0)),
	f_specialList_c tinyint NOT NULL DEFAULT ((0)),
	f_stability_c tinyint NOT NULL DEFAULT ((0)),
	f_specialList tinyint NOT NULL DEFAULT ((0)),
	f_stability tinyint NOT NULL DEFAULT ((0)),
	f_title  tinyint NOT NULL DEFAULT ((0)),
	f_internet tinyint NOT NULL DEFAULT ((0)),
	f_online tinyint NOT NULL DEFAULT ((0)),
	f_loanEquipment tinyint NOT NULL DEFAULT ((0)),
	--Score
	brcreditpoint int,
	scorecust int,
	scorebank int,
	scorep2p int,
	scorecf int,
	bankpfpoint int,
    --Title
	title tinyint,
	--Assets
	house tinyint,
	car tinyint,
	fin int,
	wealth tinyint,
	--Rating
	p2pConsumeRating nvarchar(8),
	p2pMediaRating nvarchar(8),
	p2pBrcreditRating nvarchar(8),
	--Authentication
	auth_id tinyint,
	auth_cell tinyint,
	auth_key_relation smallint,
	auth_biz_tel tinyint,
	auth_home_tel tinyint,
	auth_name tinyint,
	auth_tel_biz tinyint,
	auth_tel_home tinyint,
	auth_mail tinyint,
	auth_id_name tinyint,
	--Stability
	st_id int,
	st_cell_number int,
	st_cell_firsttime nvarchar(24),
	st_mail int,
	st_name int,
	st_tel int,
	st_addr int,
	--Brand
	b_top1 nvarchar(24),
	b_top2 nvarchar(24),
	b_top3 nvarchar(24),
	b_top4 nvarchar(24),
	b_top5 nvarchar(24),
	bfd_both_match int NOT NULL DEFAULT ((0)),
	bfd_id_match int NOT NULL DEFAULT ((0)),
	bfd_cell_match int NOT NULL DEFAULT ((0)),
	bfd_score int NOT NULL DEFAULT ((0)),
	bfd_final nvarchar(50),
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL	
)

drop table BfdMatchDataV2ApplyLoan

--AapplyLoan
CREATE TABLE BfdMatchDataV2ApplyLoan(
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	CitizenNo nvarchar(50) NOT NULL,
	Mobilephone nvarchar(50) NOT NULL,
	mon_type tinyint NOT NULL, --1:month3, 2:month6, 3:month12
	id_type tinyint NOT NULL, --1:id, 2:cell
	bank_type tinyint NOT NULL, --1:bank, 2:notbank
	selfnumber int NOT NULL DEFAULT ((0)),
	allnumber int NOT NULL DEFAULT ((0)),
	orgnumber int NOT NULL DEFAULT ((0)),
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL,
);

--Location
CREATE TABLE BfdMatchDataV2Location(
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	CitizenNo nvarchar(50) NOT NULL,
	Mobilephone nvarchar(50) NOT NULL,
	location_type tinyint NOT NULL, --1:home, 2:biz, 3:person, 4:apply, 5:other
	addr1 float, -- for example addr21
	addr2 float, -- for example addr22
	addr3 float,
	addr4 float,
	addr5 float,
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL,
);	

--Accountchange ID=110776
CREATE TABLE BfdMatchDataV2Accountchange(
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	CitizenNo nvarchar(50) NOT NULL,
	Mobilephone nvarchar(50) NOT NULL,
	cardindex smallint NOT NULL,
	regionno  int,
	mon_type smallint NOT NULL, --1:m1m3, 2:m4m6, 3:m7m9, 4:m10m12, 5:m13m15, 6:m16m18
	cred_cash int,
	cred_default int,
	cred_income int,
	cred_outgo int,
	cred_status int,
	deb_balance int,
	deb_income	 int,
	deb_outgo  int,
	deb_investment  int,
	deb_repay  int,
	loan  int,
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL,
);	


	--SpecialList_c
	id_type tinyint NOT NULL, --1:id, 2:cell, 3:gid
	filed tinyint NOT NULL, --1:bank, 2:p2p, 3:phone, 4:insurance, 5:court, 6:credit
	bad tinyint,
	overdue tinyint,
	fraud tinyint,
	lost tinyint,
	refuse tinyint,
	executed tinyint,

	--LoanEquipment

	--Flag
	flag_core_key c,
	flag_core_gid tinyint,
	flag_applyLoan tinyint,
	flag_brand tinyint,
	flag_assets tinyint,
	flag_specialList_c tinyint,
	flag_location tinyint,
	flag_stability_c tinyint,
	flag_title tinyint,
	flag_loanequipment tinyint,
	flag_consumption tinyint,
	flag_applyLoan tinyint,
	flag_score tinyint,
	flag_rulespeciallist tinyint,
	flag_ruleapplyloan tinyint,
	

CREATE TABLE BitLoan_0410.dbo.BfdConsumptionCategory (
	Name nvarchar(50) NOT NULL,
    Value smallint NOT NULL
);
drop table BfdConsumptionCategory

SELECT Name, Value FROM BfdConsumptionCategory;

delete from BfdConsumptionCategory


INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('个护化妆', 1);
INSERT INTO .BfdConsumptionCategory
(Name, Value) VALUES ('服装配饰',2);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('运动户外', 3);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('手机/手机配件', 4);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('珠宝贵金属', 5);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('母婴用品', 6);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('美食特产', 7);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('家具建材', 8);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('文化娱乐', 9);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('出差旅游', 10);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('汽车用品', 11);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('医疗保健', 12);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('数码', 13);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('箱包', 14);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('钟表首饰', 15);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('日用百货', 16);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('鞋', 17);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('收藏', 18);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('电脑/办公', 19);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('家居家纺', 20);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('家用电器', 21);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('其他', 22);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('通讯', 23);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('本地生活', 24);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('宠物生活', 25);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('网络游戏/虚拟物品', 26);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('房产', 27);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('教育培训', 28);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('保险/理财', 29);
INSERT INTO BfdConsumptionCategory
(Name, Value) VALUES ('未分类', 40);

drop table BfdMatchDataV2Consumption

CREATE TABLE BfdMatchDataV2Consumption (
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	CitizenNo nvarchar(50) NOT NULL,
	Mobilephone nvarchar(50) NOT NULL,
	mon_type smallint not null, --1: m3, 2:m6, 3:m12
	Category smallint NOT NULL,
	visits int NOT NULL,
	number int NOT NULL,
	pay int NOT NULL,
	maxpay int NOT NULL,
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL,
);
--	CONSTRAINT PK_BfdMatchDataV2Consumption PRIMARY KEY (ID)

CREATE TABLE BfdMatchDataV2ConsumptionLevel (
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	CitizenNo nvarchar(50) NOT NULL,
	Mobilephone nvarchar(50) NOT NULL,
	Catygory nvarchar(50) NOT NULL,
	level float NOT NULL,
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL,
);

CREATE TABLE BfdMediaCategory (
	Name nvarchar(50) NOT NULL,
    Value smallint NOT NULL
);
drop table BfdMediaCategory

SELECT Name, Value FROM BfdMediaCategory;

delete from BfdMediaCategory


INSERT INTO BfdMediaCategory
(Name, Value) VALUES ('历史', 1);
INSERT INTO BfdMediaCategory
(Name, Value) VALUES ('财经', 2);
INSERT INTO BfdMediaCategory
(Name, Value) VALUES ('教育', 3);
INSERT INTO BfdMediaCategory
(Name, Value) VALUES ('社区', 4);
INSERT INTO BfdMediaCategory
(Name, Value) VALUES ('母婴/育儿', 5);
INSERT INTO BfdMediaCategory
(Name, Value) VALUES ('未分类', 40);

CREATE TABLE BfdMatchDataV2Media (
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	CitizenNo nvarchar(50) NOT NULL,
	Mobilephone nvarchar(50) NOT NULL,
	mon_type smallint not null, --1: m3, 2:m6, 3:m12
	Catygory smallint NOT NULL,
	visitdays int NOT NULL,
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL,
);




