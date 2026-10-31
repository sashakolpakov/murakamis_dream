# A low-demand signed cap/CROSS contraction from the original Newton source

31 October 2026. The theorem concerns the fixed spectral pair at even levels. It retains the A-face demand, all unused factors and the genuine cutoff. It does not use a uniform-coupon semisimple model or a positive moment norm.

## 1. Original coefficients and an auxiliary full slice

Let N=2m>=4, d=N-1, M=m-1, theta=pi/N. Write

    c_r=2cos((2r+1)theta), a_r=2+c_r,
    gamma_r=2-c_r, s_r=2sin(r theta),
    P_r=product_(j=1)^r s_j, P_0=1.

Use the original C_(j,h), U_j and V_j from the [original-demand convolution](research_two_port_main_cap_original_demand_convolution.md), extending their literal formulas to all 0<=j,h<=d where meaningful. In particular

    C_(j,h)=[A^j Z^(d-h-j)] K_(d-h)(A,Z)
                         product_(r=d-h+1)^d a_r,
    U_j=4 P_j^2/product_(r=0)^j gamma_r,
    V_j=4 P_j^2/product_(r=0)^j a_r,
    C_(0,n)=N^2 product_(r=0)^(n-1)a_r/P_n^2
           =V_(d-n).                                      (1)

For every 0<=n<=d define only as an algebraic auxiliary

    S_n^full=sum_(j=0)^n (-1)^j U_j C_(j,n-j).               (2)

For 0<=n<=M this is exactly the original projected cap/CROSS sum S_(N,n), because its J_n is 0..n. No equality with the projected sum is asserted for n>M.

The new identity is

    gamma_n S_n^full+s_n^2 S_(n-1)^full=4 C_(0,n),
    0<=n<=d, S_(-1)^full=0.                               (3)

In particular it keeps the original top-boundary coefficient that was undetermined by the previous C_(j,h) recurrence.

## 2. Literal three-port completion and its turn dictionary

Use the actual two-bridge slot word [1,0,1], with first top cap marked. Its ordered face quartets are

    E=(A,u,C,Z), F=(u,A,v,C), G=(v,C,u,Z),

with protected faces u=v=0. At E put the actual V_N(-2), at F the actual V_N(2), and at G put

    g_n(Omega)=product_(r=0)^(n-1)(Omega-c_r).

The specialization of G is (0,C,0,Z). In the original face operator, (-T-c_(d-r)) acting on C^(d-r) has only the monomer transition -s_(d-r)^2 Z C^(d-r-1). Since c_(d-r)=c_r and s_(d-r)=s_(r+1), successive factors give EXACTLY

    H_(g_n)(0,C,0,Z)=(-1)^n P_n^2 C^(d-n) Z^n.              (4)

Thus the unchanged targets A^d C^d Z^d select (2), and the raw marked scalar of this three-port completion is

    Z(E,F,g_n)=(-1)^(d+n) P_n^2 S_n^full
             =(-1)^(n+1) P_n^2 S_n^full.                   (5)

Here the raw E(-2) source is (-1)^d times its positive endpoint polynomial. The full F(2) monomer coefficient is (-1)^j U_j. Equation (4) is a genuine polynomial coupon, not a sector projector.

For completeness the exact rational-tangle dictionary needed below is

    Z(E,F,G)=phi(G R(F R(E))),                              (6)

where R is the genuine UNSCALED original quarter-turn and
phi(B)=N^-1 Tr[(I tensor g)B] is the original marked Frobenius functional. This identity includes all original turns and their scalar factors. It can be verified directly as follows. Put x=q^d. Label the bottom physical pairs (s,d-s),(b,d-b); the successive box entries are

    E_(t,v;d-s,b), F_(d-a,u;s,t), G_(a,b;u,v).

The unwrapped conservation laws force the first top pair to be (d-a,a). Two original cups, the first marked cap and the remaining ordinary cap contribute

    N^-1 x^(s+a+2b-2d).

On the right side of (6), expand

    R(B)_(a,b;c,e)=x^(a-e) B_(d-a,c;b,d-e),
    g_b=x^(2b-d).

Expanding the right side of (6) in its literal matrix order first gives

    N^-1 sum x^(u+h+2b-2d) G_(a,b;u,v)
                  F_(d-u,a;h,k) E_(d-h,v;k,b).

The actual root pair Casimir, and hence every polynomial F in it, is symmetric and invariant under the simultaneous swap/complement J(a,b)=(d-b,d-a). Explicitly,

    F_(r,s;p,t)=F_(p,t;r,s)
              =F_(d-s,d-r;d-t,d-p).

The latter identity can be checked directly on the original diagonal and two transition entries: under U->Q^-1 V^-1, V->Q^-1 U^-1, the diagonal and corresponding upward/downward transition coefficients are unchanged. It then holds for all powers and polynomials, including every Jordan component. Apply both identities to obtain

    F_(d-u,a;h,k)=F_(d-a,u;d-k,d-h).

Set s=d-k, t=d-h. The E entry becomes exactly E_(t,v;d-s,b). Unwrapped conservation in this F entry gives d-a+u=s+t, so its phase becomes

    x^(u+h+2b-2d)=x^(s+a+2b-2d).

Thus all three matrix entries and the original turn/mark factor agree term by term with the physical contraction above. This proves (6) before spectral evaluation or the Newton change of coordinates. No generic semisimple recoupling or reset mark is used.

## 3. Original Newton algebra gives the recurrence

Use the [genuine Newton packet](actual_newton_turn_positive_gram.md)

    Bhat_r(z)=product_(j=0)^(r-1)(c_j-z)/P_r^2,
    R Bhat_r=Bhat_(d-r),
    phi(Bhat_i Bhat_j)=1_(i+j=d).

Multiplication by z in these coordinates is the full lower-bidiagonal matrix Z_N:

    (Z_N)_(r,r)=c_r,
    (Z_N)_(r,r-1)=-s_r^2,
    Z_N^T=P_rev Z_N P_rev.                              (7)

All repeated roots and Jordan data remain. If alpha_E is the Newton coefficient column of E, then (6) and the displayed transpose relation imply

    Z(E,F,G)=alpha_E^T F(Z_N) P_rev alpha_G.               (8)

For E=V_N(-2) the divided-difference formula for the ACTUAL numerator gives

    (alpha_E)_r=-V_r.

Indeed chi_N(-2)=4 at even levels, and the coefficient is
4(-1)^r P_r^2/product_(j=0)^r(-2-c_j)=-V_r. For G=g_n,

    alpha_G=(-1)^n P_n^2 e_n.

For F=V_N(2), the FULL minimal-polynomial identity chi_N(Z_N)=0 gives

    F(Z_N)=4(2I-Z_N)^(-1),                               (9)

because chi_N(2)=4 and every gamma_r>0. Combining (5),(8),(9) cancels the exact nonzero factor (-1)^(n+1)P_n^2 and yields

    S_n^full=V^T [4(2I-Z_N)^(-1)] e_(d-n).                (10)

Let w^T=V^T[4(2I-Z_N)^(-1)]. Its defining identity
w^T(2I-Z_N)=4V^T gives

    gamma_j w_j+s_(j+1)^2 w_(j+1)=4V_j.

Set j=d-n and use (1), c_(d-n)=c_n, and s_(d-n+1)=s_n. This is exactly (3). No norm estimate or total-variation bound for this inverse has been inserted.

Equivalently, the explicit inverse of the bidiagonal matrix gives

    S_n^full=4 sum_(h=0)^n (-1)^(n-h) C_(0,h)
              product_(r=h+1)^n s_r^2
                         /product_(r=h)^n gamma_r.       (11)

This is an exact fixed-pair signed summation identity, with cancellation retained.

## 4. A macroscopic low-demand contraction

Define the same normalized scalar as the fixed-resolvent reduction,

    R_n=gamma_n S_n^full/(4 C_(0,n)).

Since C_(0,n)/C_(0,n-1)=a_(n-1)/s_n^2, (3) becomes the INHOMOGENEOUS scalar recurrence

    R_0=1,
    R_n=1-t_n R_(n-1),
    t_n=s_n^4/[a_(n-1)gamma_(n-1)]
       =4sin^4(n theta)/sin^2((2n-1)theta).              (12)

The n=0 convention agrees with the original R definition. This is not a scalar orthogonal-polynomial assertion.

For every even N>=4,

    |R_n|<=1, 0<=n<=floor(N/4).                         (13)

Here is a direct proof, including the small levels. The positive function
t(v)=4sin^4(v theta)/sin^2((2v-1)theta) is increasing for 1<=v<=M: its logarithmic derivative is
4theta[cot(v theta)-cot((2v-1)theta)]>=0. If N=4k+2, then theta<=pi/6 and

    t_k=(1-sin theta)^2/cos^2(2theta)<=1,

because sin theta<=1/2. Thus all k successive maps in (12) preserve [0,1]. If N=4k, every n<=k-1 has t_n<=1 by comparison with v=k-1/2 (for k>=2 the same preceding inequality applies). The final coefficient is t_k=sec^2 theta<=2. Therefore the first k-1 values lie in [0,1], and R_k belongs to [1-sec^2 theta,1] subset [-1,1]. At N=4 there is no preliminary step and R_1=-1 directly. At N=6, R_1=0. This proves (13).

Throughout this range n<=M, the full slice is the genuine original projected sum. Its endpoint comparator D_(N,n) is a sum of positive terms and contains V_0 C_(0,n), where V_0=4/a_0. Hence

    |S_(N,n)| <=4 C_(0,n)/gamma_n
               <=[a_0/gamma_n] D_(N,n)
               <=N^2 D_(N,n),
    0<=n<=floor(N/4).                                  (14)

The sharper factor a_0/gamma_n is bounded independently of N on every fixed macroscopic interval rho N<=n<=N/4, rho>0. The raw coefficient differs only by (-1)^d. The original A^d extraction and remaining C,Z exponents have not changed.

## 5. Exact scope and validation

Equation (3) holds for the full auxiliary slices, while the bound (14) applies to the original projected cap/CROSS coefficient in the stated low-demand range at even levels. It is complementary to the separately proved [high-demand theorem](research_cap_cross_high_demand_signed_contraction.md). It does not yet cover N/4<n<=M, the middle cutoffs n>M, or the odd-level source. The forward recurrence can be unstable when t_n>1, so (13) must not be extrapolated without a further argument. A simple uniform bound for the actual full inverse in (10) is neither proved nor required.

The proof inputs are the original-demand convolution, the [full homogeneous face theorem](actual_homogeneous_casimir_face_source.md), the literal root swap/complement symmetry, and the genuine Newton turn/Frobenius identities. The literal physical-index verification (6) supplies the source adapter. A focused independent direct calculation of the original K recurrence at 90 digits checked (3) for all full slices at N=4,6,8,10,12,16,20 (76 coefficients); maximum relative residual below 6e-81. This is a finite identity check, not the proof of the general estimate. A separate [portable exact-field audit](../experiments/audit_research_cap_cross_low_demand_newton_contraction.py), with [recorded results](../experiments/research_cap_cross_low_demand_newton_contraction_results.json), independently contracts the actual three-port physical tensors at four even levels. It verifies 28 original marked scalars, 28 full auxiliary recurrences, 14 original low-cutoff identifications and 28 Newton resolvent entries. These finite checks support the source dictionary; inequality (14) is proved analytically above.

The stated low-demand range and parity restrictions remain essential. In particular, the omitted top coefficient belongs to the actual source and cannot be restored from an auxiliary recurrence.

Additional source reference: [full physical pair commutant and genuine marked trace](actual_pair_casimir_commutant_and_rotated_trace.md), sections 2–4.
