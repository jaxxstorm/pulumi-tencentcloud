// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Emr.Outputs
{

    [OutputType]
    public sealed class NodesNodeResult
    {
        public readonly int AppId;
        public readonly string ApplyTime;
        public readonly int AutoFlag;
        public readonly string CdbIp;
        public readonly ImmutableArray<Outputs.NodesNodeCdbNodeInfoResult> CdbNodeInfos;
        public readonly int CdbPort;
        public readonly int ChargeType;
        public readonly int CpuNum;
        public readonly int Destroyable;
        public readonly string DeviceClass;
        public readonly string DiskSize;
        public readonly string DynamicPodSpec;
        public readonly string EmrResourceId;
        public readonly string ExpireTime;
        public readonly int Flag;
        public readonly string FreeTime;
        public readonly string HardwareResourceType;
        public readonly int HwDiskSize;
        public readonly string HwDiskSizeDesc;
        public readonly int HwMemSize;
        public readonly string HwMemSizeDesc;
        public readonly string Ip;
        public readonly int IsAutoRenew;
        public readonly int IsDynamicSpec;
        public readonly ImmutableArray<Outputs.NodesNodeMcMultiDiskResult> McMultiDisks;
        public readonly string MemDesc;
        public readonly int MemSize;
        public readonly int Mutable;
        public readonly string NameTag;
        public readonly string OrderNo;
        public readonly int RegionId;
        public readonly int RootSize;
        public readonly string SerialNo;
        public readonly string Services;
        public readonly string Spec;
        public readonly int StorageType;
        public readonly int SupportModifyPayMode;
        public readonly ImmutableArray<Outputs.NodesNodeTagResult> Tags;
        public readonly string WanIp;
        public readonly int ZoneId;

        [OutputConstructor]
        private NodesNodeResult(
            int appId,

            string applyTime,

            int autoFlag,

            string cdbIp,

            ImmutableArray<Outputs.NodesNodeCdbNodeInfoResult> cdbNodeInfos,

            int cdbPort,

            int chargeType,

            int cpuNum,

            int destroyable,

            string deviceClass,

            string diskSize,

            string dynamicPodSpec,

            string emrResourceId,

            string expireTime,

            int flag,

            string freeTime,

            string hardwareResourceType,

            int hwDiskSize,

            string hwDiskSizeDesc,

            int hwMemSize,

            string hwMemSizeDesc,

            string ip,

            int isAutoRenew,

            int isDynamicSpec,

            ImmutableArray<Outputs.NodesNodeMcMultiDiskResult> mcMultiDisks,

            string memDesc,

            int memSize,

            int mutable,

            string nameTag,

            string orderNo,

            int regionId,

            int rootSize,

            string serialNo,

            string services,

            string spec,

            int storageType,

            int supportModifyPayMode,

            ImmutableArray<Outputs.NodesNodeTagResult> tags,

            string wanIp,

            int zoneId)
        {
            AppId = appId;
            ApplyTime = applyTime;
            AutoFlag = autoFlag;
            CdbIp = cdbIp;
            CdbNodeInfos = cdbNodeInfos;
            CdbPort = cdbPort;
            ChargeType = chargeType;
            CpuNum = cpuNum;
            Destroyable = destroyable;
            DeviceClass = deviceClass;
            DiskSize = diskSize;
            DynamicPodSpec = dynamicPodSpec;
            EmrResourceId = emrResourceId;
            ExpireTime = expireTime;
            Flag = flag;
            FreeTime = freeTime;
            HardwareResourceType = hardwareResourceType;
            HwDiskSize = hwDiskSize;
            HwDiskSizeDesc = hwDiskSizeDesc;
            HwMemSize = hwMemSize;
            HwMemSizeDesc = hwMemSizeDesc;
            Ip = ip;
            IsAutoRenew = isAutoRenew;
            IsDynamicSpec = isDynamicSpec;
            McMultiDisks = mcMultiDisks;
            MemDesc = memDesc;
            MemSize = memSize;
            Mutable = mutable;
            NameTag = nameTag;
            OrderNo = orderNo;
            RegionId = regionId;
            RootSize = rootSize;
            SerialNo = serialNo;
            Services = services;
            Spec = spec;
            StorageType = storageType;
            SupportModifyPayMode = supportModifyPayMode;
            Tags = tags;
            WanIp = wanIp;
            ZoneId = zoneId;
        }
    }
}
