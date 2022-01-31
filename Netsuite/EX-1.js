/************************************************************************
 * Copyright (c) 2014-2021 USA Sealing, LLC.

 *
 * The following JavaScript source code is created by USA Sealing, LLC and
 * is intended for use on the NetSuite (www.netsuite.com) platform.

 *
 * Company: USA Sealing, LLC (www.USA Sealing.com)


 ***********************************************************************
 * 
 * @NApiVersion 2.x
 * @NScriptType userEventScript
**/

define(['N/record'], function (record) {


    function afterSubmit(context) {
        var logTitle = 'afterSubmit()';
        try {
            var recordType = context.newRecord.type;
            if (recordType == 'itemfulfillment') {

                var recItemFulfillment = context.newRecord || context.oldRecord;
                var salesOrderId = recItemFulfillment.getValue('createdfrom');

                if (!isEmpty(salesOrderId)) {
                    var recSalesOrder = record.load({
                        type: 'salesorder',
                        id: salesOrderId
                    });

                    var blShipDateChanged = updateShipDate(recSalesOrder);

                    if (blShipDateChanged) {
                        recSalesOrder.save({
                            enableSourcing: true,
                            ignoreMandatoryFields: true
                        });
                    }
                }
            }

        } catch (error) {
            log.error(logTitle, error);
        }
    }

    function updateShipDate(recSalesOrder) {
        var logTitle = 'updateShipDate()';
        try {
            var soShipDate = recSalesOrder.getValue('shipdate');
            var earliestExpectedShipDate = getEarliestExpectedShipDate(recSalesOrder);
            var blShipDatesAreDifferent = soShipDate != earliestExpectedShipDate;

            if (!isEmpty(earliestExpectedShipDate) && blShipDatesAreDifferent) {
                recSalesOrder.setValue('shipdate', earliestExpectedShipDate);
            }

            return blShipDatesAreDifferent;

        } catch (error) {
            log.error(logTitle, error);
        }
    }


    function getEarliestExpectedShipDate(currentRecord) {
        var logTitle = 'getEarliestExpectedShipDate()';
        try {
            var dtEarlistExpectedShipDate = null;

            var itemSublistLineCount = currentRecord.getLineCount('item');
            for (var i = 0; i < itemSublistLineCount; i++) {

                var lineOrderQuantity = currentRecord.getSublistValue({
                    sublistId: 'item',
                    fieldId: 'quantity',
                    line: i
                });
                var lineFulfilledQuantity = currentRecord.getSublistValue({
                    sublistId: 'item',
                    fieldId: 'quantityfulfilled',
                    line: i
                });


                if (lineFulfilledQuantity < lineOrderQuantity) {

                    var lineEarlistExpectedShipDate = currentRecord.getSublistValue({
                        sublistId: 'item',
                        fieldId: 'expectedshipdate',
                        line: i
                    });


                    if (isEmpty(dtEarlistExpectedShipDate) && !isEmpty(lineEarlistExpectedShipDate)) {
                        dtEarlistExpectedShipDate = lineEarlistExpectedShipDate;
                    }


                    if (!isEmpty(lineEarlistExpectedShipDate) && !isEmpty(dtEarlistExpectedShipDate)
                        && lineEarlistExpectedShipDate < dtEarlistExpectedShipDate) {
                        dtEarlistExpectedShipDate = lineEarlistExpectedShipDate;
                    }
                }
            }

            return dtEarlistExpectedShipDate;

        } catch (error) {
            log.error(logTitle, error);
        }
    }


    function isEmpty(value) {
        var logTitle = 'isEmpty()';
        try {
            if (value == null || value == '' || (!value) || value == 'undefined') {
                return true;
            }
            return false;
        } catch (error) {
            log.error(logTitle, error);
        }
    };

    return {
        afterSubmit: afterSubmit
    }
});