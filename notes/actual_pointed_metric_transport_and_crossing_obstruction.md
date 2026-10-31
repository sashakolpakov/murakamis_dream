# Pointed metric certificates and the cost of a modulus crossing

28 October 2026. A varying positive metric gives an exact transport
certificate for the original source. It is useful only when its source
cost and conditioning are bounded independently. A concrete two-channel
calculation below shows that a full-space quadratic certificate with
subexponential conditioning can still be forced to pay the pointwise
spectral envelope, even for a specified single input and output. Thus
source endpoint costs alone do not recover coherent phase cancellation.

This complements, and does not reprove,
[the exact Gaussian conversion example](analytic_two_channel_conversion_counterexample.md).
The example is an analytic matrix cocycle, not an actual knot operator.
The final section states a source-specific adjoint certificate whose
geometric construction remains open.

## 1. Exact metric and cocycle statements

Let v_(j+1)=T_j v_j, j=0,...,n-1, with original input v_0=s
and original output A=l^*v_n. For positive definite Hermitian H_j,

    T_j^*H_(j+1)T_j <= exp(2h_j) H_j              (1)

is equivalent, by taking square roots, to

    ||H_(j+1)^(1/2) T_j H_j^(-1/2)||<=exp(h_j).

There is no scalarity or unitarity assumption. Iteration gives

    |A| <= exp(sum h_j)
                   sqrt[(s^*H_0s)(l^*H_n^(-1)l)]. (2)

All actual external source factors multiply (2) unchanged. Applied
to the actual recurrence in
[the macroscopic source theorem](actual_macroscopic_a_spectral_upper_bound.md),
the certificate must be uniform on its specified tiny complex-q
circle. Its entire original initial color packet is s; it cannot
be replaced by a truncated normal Taylor series.

The usual finite-horizon Gramian clarifies what (1) proves. Normalize
A_j=exp(-h_j)T_j and write P_(k:j)=A_(k-1)...A_j, P_(j:j)=I.
If ||P_(k:j)||<=B_N for EVERY subinterval, then

    H_j=sum_(k=j)^n P_(k:j)^*P_(k:j)
       =I+A_j^*H_(j+1)A_j,
    I<=H_j<=(n-j+1)B_N^2 I.                       (3)

Conversely a certificate I<=H_j<=C_N I bounds every normalized
subproduct by sqrt(C_N). Thus a uniformly tame full-space Gramian
is essentially equivalent to a tame bound for ALL subproducts,
not merely the selected full scalar. Formula (3), constructed from
unknown products, is an equivalence and not a new geometric estimate.

Scalar rescalings of H_j move telescoping scalar terms into h_j.
They do not remove anisotropic condition numbers; the endpoint
source factor in (2) must always be retained.

There is an exact test using ANY fixed partition of the time interval.
Let P_i be its subproducts and let J list the partition nodes,
including both endpoints. The logarithmic right side B of (2) obeys

    B>=sum_i log||P_i||+log(||s|| ||l||)
                              -1/2 sum_(j in J) log cond H_j.  (3a)

Indeed each interval costs at least log||P_i|| minus its endpoint
metric ratio. Interior scalar ratios telescope, leaving the displayed
condition numbers. The source costs satisfy
s^*H_0s>=lambda_min(H_0)||s||^2 and
l^*H_n^(-1)l>=||l||^2/lambda_max(H_n), proving (3a).
Thus tame full metrics cannot hide known large subinterval norms.
An actual source norm which is exponentially small is still retained
in (3a); no lower bound on an unknown color packet is assumed.

## 2. An exact lower bound on every positive quadratic certificate

Suppose each T_j is upper triangular in one fixed orthonormal basis.
Split at an arbitrary m and write P_pre=T_(m-1)...T_0 and
P_post=T_(n-1)...T_m. Their diagonal entries have the form

    e_2^*P_pre=D_pre e_2^*, P_post e_1=A_post e_1.

Keep the actual source s=e_2 and l=e_1, not an operator norm source.
Define the full bound furnished by (2) as

    B=sum_j h_j+1/2 log[(H_0)_(22)(H_n^(-1))_(11)].

Then EVERY positive definite certificate (1) satisfies exactly

    B >= log|D_pre A_post|-1/2 log cond(H_m).       (4)

Proof. The pre-product inequality, in its dual norm, gives

    |D_pre|^2 (H_0^(-1))_(22)
                   <=exp(2h_pre)(H_m^(-1))_(22).

Since H_(22)(H^(-1))_(22)>=1, this implies

    (H_0)_(22)>=exp(-2h_pre)|D_pre|^2/(H_m^(-1))_(22).

The post-product inequality on e_1 gives

    (H_n^(-1))_(11)
                   >=exp(-2h_post)|A_post|^2/(H_m)_(11).

Multiply, and use
(H_m)_(11)(H_m^(-1))_(22)<=cond(H_m). This proves (4).
Neither endpoint is required to be comparable to the identity;
their EXACT actual-source costs are already included in B.

## 3. Distinct expanding roots still force the envelope cost

Use the analytic cocycle from the cited conversion proof, allowing
a harmless common positive multiplier exp(c):

    T_(N,j)=exp(c) [[exp(a(j/N-1/2)), N^(-p)],
                    [0,exp(-a(j/N-1/2)+i theta)]],
    0<theta<min(a,pi), p fixed, j=0,...,N-1.      (5)

Its two eigenvalues are distinct at every real x and their moduli
cross at x=1/2. Choosing c>a/2 makes BOTH roots expanding everywhere.
The separately proved exact Gaussian computation gives

    lim (1/N)log|e_1^*P_N e_2|
       =c+Gamma, Gamma=a/4-theta^2/(4a)>0.       (6)

Each complete marked eigenbranch instead has rate c. The pointwise
spectral envelope has rate c+a/4. No real eigenvalue collision is
involved in these different quantities.

Take m=ceil(N/2). Directly summing the two diagonal logarithms gives

    log|D_pre A_post|=N(c+a/4)+O(1/N).

Therefore (4) yields

    B/N >=c+a/4-(log cond H_m)/(2N)+O(N^(-2)).    (7)

If log cond H_m=o(N), this FULL-SPACE quadratic certificate pays at
least the scalar envelope, although the actual selected amplitude
has the smaller rate (6). To reach its true rate with (1)--(2),

    log cond H_m >= N theta^2/(2a)-o(N).          (8)

Exponential anisotropy is thus necessary for that improvement.
This is not a zero-source example or an appeal to a backward metric.
It applies to the nonzero, explicitly calculated source in (6).
The same issue can occur at a modulus-only crossing such as the
independently derived 6_1 quartic; this does NOT assert that the
model cocycle (5) is its actual quantum recurrence.

## 4. What a source-restricted certificate would need

A semidefinite observable Gramian can exclude irrelevant directions.
If H_n>=ll^* and T_j^*H_(j+1)T_j<=exp(2h_j)H_j, then

    |A|^2<=exp(2 sum h_j) s^*H_0s.               (9)

The rank-one choice H_j=w_jw_j^* with the EXACT backward adjoint
w_j=T_j^*w_(j+1), w_n=l satisfies equality. Its initial pairing is
the UNKNOWN answer itself. Likewise restricting to the exact forward
trajectory line gives condition number one but requires knowing that
trajectory. Neither observation supplies the missing estimate.

There is, however, a useful independently checkable residual criterion.
Give explicit candidate adjoint vectors w_j with w_n=l and defects

    r_j=w_j-T_j^*w_(j+1).

For the original forward state one has the exact identity

    A=w_0^*s-sum_(j=0)^(n-1) r_j^*v_j.           (10)

Thus any proved forward bounds ||v_j||<=B_j imply

    |A|<=|w_0^*s|+sum_j B_j ||r_j||.             (11)

The safe spectral-envelope theorem already supplies forward bounds
of this kind on its actual denominator-avoiding circle. To improve
the final exponent, one must CONSTRUCT w_j whose original boundary
pairing and weighted residual sum in (11) have the desired geometric
rate. Algebraic WKB candidates and their finite-difference residuals
can be tested directly; merely taking formal O(1/N) residuals does
not suffice when B_j is exponentially large.

The equivalent positive defect estimate is also explicit: for eta>0,

    T_j^*w_(j+1)w_(j+1)^*T_j
        <=(1+eta)w_jw_j^*+(1+eta^(-1))r_jr_j^*.

It retains the entire residual observable rather than inserting an
uncontrolled positive completion of a rank-one metric. The Gaussian
conversion example shows that those residuals may encode a genuine
additional exponential branch action. Distinct roots and a real
modulus gap alone cannot justify deleting it.

The unproved geometric gate is therefore explicit source-compatible
adjoint/filtration transport, including conversion terms at complex
turning points and the actual boundary source. Full-space positive
metrics with subexponential conditioning cannot be presumed to
provide that improvement. Source-dependent nonquadratic methods,
explicitly controlled exponential metrics, and a genuinely verified
semidefinite adjoint certificate remain possible.

[Audit](../experiments/audit_actual_pointed_metric_transport.py)
checks the exact metric inequalities, their pointed lower bound,
the finite Gramian identity and the adjoint residual formula.
