
drop table AnRongCreditReportDecode

CREATE TABLE AnRongCreditReportDecode (
	ID bigint NOT NULL IDENTITY (1,1) PRIMARY KEY,
	CustomerName nvarchar(50) NOT NULL,
	PaperNumber nvarchar(50) NOT NULL,
	ReportTime datetime NOT NULL,
	--account-normal--
	acc_wjq_num int NOT NULL,
	acc_jq_num int NOT NULL,
	acc_total int NOT NULL,
	acc_amount float NOT NULL DEFAULT ((0)),
	--account-abnormal--
	acc_ewjq_num int NOT NULL,
	acc_ejq_num int NOT NULL,
	acc_etotal int NOT NULL,
	acc_eamount float NOT NULL DEFAULT ((0)),
	--apply--
	apy_doing_num int NOT NULL,
	apy_pass_num int NOT NULL,
	apy_reject_num int NOT NULL,
	apy_cancel_num int NOT NULL DEFAULT ((0)),
	apy_total int NOT NULL,
	--query--
	apy_query_total int NOT NULL,
	apy_query_total_bjg int NOT NULL DEFAULT ((0)),
	apy_query_total_fbjg int NOT NULL DEFAULT ((0)),
	--black--
	blk_num int NOT NULL DEFAULT ((0)),
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL,
);

CREATE INDEX PK_AnRongCreditReportDecode ON AnRongCreditReportDecode (ID);

