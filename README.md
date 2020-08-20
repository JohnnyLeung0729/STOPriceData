# STOPriceData
STO站点报价信息获取功能程序

通过api接口读取json数据，进行整理后，根据id获取明细数据，并将所有数据存储到对应的mysql数据库

数据库结构如下：
CREATE TABLE `pricelist` (
  `id` varchar(128) NOT NULL,
  `priceid` varchar(128) DEFAULT NULL,
  `provname` varchar(128) DEFAULT NULL,
  `provid` varchar(128) DEFAULT NULL,
  `cityname` varchar(128) DEFAULT NULL,
  `cityid` varchar(128) DEFAULT NULL,
  `weirog` varchar(128) DEFAULT NULL,
  `pricemodel` varchar(128) DEFAULT NULL,
  `wetmodel` varchar(128) DEFAULT NULL,
  `piecePrice` varchar(128) DEFAULT NULL,
  `continuedHeavy` varchar(128) DEFAULT NULL,
  `continuedHeavyPrice` varchar(128) DEFAULT NULL,
  `surcharge` varchar(128) DEFAULT NULL,
  `lowestPrice` varchar(128) DEFAULT NULL,
  `weightModeNameG` varchar(128) DEFAULT NULL,
  `weightCarriesNumberG` varchar(128) DEFAULT NULL,
  `weightDiscardsNumberG` varchar(128) DEFAULT NULL,
  `weightModeParameterG` varchar(128) DEFAULT NULL,
  `ykg` varchar(128) DEFAULT NULL,
  `ykgPrice` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


CREATE TABLE `zd_base_info` (
  `cusnum` varchar(128) DEFAULT NULL,
  `priceid` varchar(128) NOT NULL,
  `pricename` varchar(128) DEFAULT NULL,
  `pricenum` varchar(128) DEFAULT NULL,
  `pricewebadd` varchar(128) DEFAULT NULL,
  `parcusnum` varchar(128) DEFAULT NULL,
  `parcusname` varchar(128) DEFAULT NULL,
  `usestatus` varchar(128) DEFAULT NULL,
  `singstatus` varchar(128) DEFAULT NULL,
  `sortnum` varchar(128) DEFAULT NULL,
  `pricetype` varchar(128) DEFAULT NULL,
  `trntype` varchar(128) DEFAULT NULL,
  `ordertype` varchar(128) DEFAULT NULL,
  `ordmodel` varchar(128) DEFAULT NULL,
  `protype` varchar(128) DEFAULT NULL,
  `cc` varchar(128) DEFAULT NULL,
  `ccnum` varchar(128) DEFAULT NULL,
  `mc` varchar(128) DEFAULT NULL,
  `mcnum` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`priceid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8