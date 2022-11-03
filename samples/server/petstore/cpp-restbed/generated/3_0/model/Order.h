/**
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI-Generator 6.3.0-SNAPSHOT.
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * Order.h
 *
 * 
 */

#ifndef Order_H_
#define Order_H_



#include <string>
#include <memory>
#include <vector>
#include <array>
#include <boost/property_tree/ptree.hpp>
#include "helpers.h"

namespace org {
namespace openapitools {
namespace server {
namespace model {

/// <summary>
/// 
/// </summary>
class  Order 
{
public:
    Order() = default;
    explicit Order(boost::property_tree::ptree const& pt);
    virtual ~Order() = default;

    Order(const Order& other) = default; // copy constructor
    Order(Order&& other) noexcept = default; // move constructor

    Order& operator=(const Order& other) = default; // copy assignment
    Order& operator=(Order&& other) noexcept = default; // move assignment

    std::string toJsonString(bool prettyJson = false) const;
    void fromJsonString(std::string const& jsonString);
    boost::property_tree::ptree toPropertyTree() const;
    void fromPropertyTree(boost::property_tree::ptree const& pt);


    /////////////////////////////////////////////
    /// Order members

    /// <summary>
    /// 
    /// </summary>
    int64_t getId() const;
    void setId(int64_t value);

    /// <summary>
    /// 
    /// </summary>
    int64_t getPetId() const;
    void setPetId(int64_t value);

    /// <summary>
    /// 
    /// </summary>
    int32_t getQuantity() const;
    void setQuantity(int32_t value);

    /// <summary>
    /// 
    /// </summary>
    std::string getShipDate() const;
    void setShipDate(std::string value);

    /// <summary>
    /// Order Status
    /// </summary>
    std::string getStatus() const;
    void setStatus(std::string value);

    /// <summary>
    /// 
    /// </summary>
    bool isComplete() const;
    void setComplete(bool value);

protected:
    int64_t m_Id = 0L;
    int64_t m_PetId = 0L;
    int32_t m_Quantity = 0;
    std::string m_ShipDate = "";
    std::string m_Status = "";
    bool m_Complete = false;
};

std::vector<Order> createOrderVectorFromJsonString(const std::string& json);

template<>
inline boost::property_tree::ptree toPt<Order>(const Order& val) {
    return val.toPropertyTree();
}

template<>
inline Order fromPt<Order>(const boost::property_tree::ptree& pt) {
    Order ret;
    ret.fromPropertyTree(pt);
    return ret;
}

}
}
}
}

#endif /* Order_H_ */
