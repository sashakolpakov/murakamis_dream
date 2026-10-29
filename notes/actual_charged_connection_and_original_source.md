# The actual endpoint q-connection, clock feedback and its source extension

28 October 2026. The charged polynomial has a flat rank-one q-connection
whose numerator and denominator degrees are bounded by the diagram
valencies, independently of N. Macroscopic lengths Q^L are retained.
Its correct source Ward identity uses a specified endpoint-DELETED
polynomial. It is not a polynomial annihilator of the top-degree state
obtained by simply multiplying the cleared equation by that state.

The original clock feedback has an exact compatible mixed transport.
These identities retain all macro defects and peripheral factors, but
they do NOT imply a nonzero selected geometric component. We locate
precisely the information lost by localizing the actual nilpotent source.

## 1. Exact bounded-degree endpoint connection

Use the original charged source, before or after its exact closure
contractions, with d=N-1 and Q primitive of order N. Write its fixed-clock
polynomial, including every extracted nonzero scalar, as

    P_h=gamma_h product_i X_i^(mu_i)
                     product_e B_(L_e)(X_(u_e),X_(v_e);a_e),
    B_L(U,V;a)=product_(r=0)^(L-1)(U-Q^r aV).           (1)

Nonloop blocks have u_e!=v_e, 1<=L_e<=d. Actual self-loops have
been evaluated as their exact scalar times X_i^L; a zero scalar means
the actual sector is zero and is not localized. All gamma_h, original
clock factors W_h, chi_N, pivots and Cartan/framing phases remain.
The original functional is lambda(P)=[product_i X_i^d]P.

Let tau_i shift X_i to QX_i. The literal block ratios are

    B_L(Q U,V;a)/B_L(U,V;a)
                  =Q^L (U-Q^(-1)aV)/(U-Q^(L-1)aV),
    B_L(U,Q V;a)/B_L(U,V;a)
                  =(U-Q^L aV)/(U-aV).                 (2)

Define

    D_i=product_(u_e=i)(X_i-Q^(L_e-1)a_e X_(v_e))
             *product_(v_e=i)(X_(u_e)-a_e X_i),
    N_i=Q^(mu_i+sum_(u_e=i)L_e)
          product_(u_e=i)(X_i-Q^(-1)a_e X_(v_e))
             *product_(v_e=i)(X_(u_e)-Q^(L_e)a_e X_i). (3)

Then EXACTLY in the ordinary polynomial ring,

    D_i tau_i P_h=N_i P_h.                           (4)

Each degree is the number of incident nonloop BLOCKS, not the sum of
their lengths. It is bounded for a fixed diagram. The Q^L coefficients
are not replaced by one when L is proportional to N. Self-loops
contribute the displayed Q^mu, rather than being counted twice in (2).

On the regular locus these ratios define a flat rank-one connection:

    R_i=N_i/D_i=tau_i P_h/P_h,
    (tau_j R_i)R_j=(tau_i R_j)R_i,
    product_(r=0)^(N-1) tau_i^r R_i=1.                (5)

These are actual identities with a specified global section P_h.
Flatness by itself is not new knot holonomy or a source nonvanishing
theorem. In particular (5) has no extra condition on Fermat centers.

## 2. The NONTRIVIAL original source current

Every factor of D_i in (3) is the last factor of an outgoing block or
the first factor of an incoming block. Therefore D_i divides the
ordinary polynomial P_h, with multiplicities as specified by its
factorization. Put

    P_(h,i)^del=P_h/D_i.                              (6)

This is an endpoint-deletion operation on the proved polynomial, not
an inverse in the nilpotent algebra. Equation (4) is equivalently

    tau_i P_h=N_i P_(h,i)^del.

Since lambda(tau_i P)=Q^d lambda(P), the exact source current is

    lambda((N_i-Q^d D_i)P_(h,i)^del)=0.              (7)

For a Laurent-polynomial insertion F its retained version is

    lambda(F N_i P_(h,i)^del)
                 =Q^d lambda((tau_i^(-1)F) P_h).     (8)

The coefficient here is the specified Laurent-residue source whenever
F has negative exponents. No claim that arbitrary such insertions are
original finite-head coupons is needed. At F=1 equation (7) preserves
the original charge and is already nontrivial.

In contrast, lambda((N_i-Q^dD_i)P_h)=0 is normally VACUOUS: the inserted
homogeneous numerator has positive degree and P_h is already at the
total top degree. Confusing it with (7) loses the actual endpoint source
extension. Equation (7) survives multiplication by the full W_h and
summation over the actual clocks, with its h-dependent coefficients
and endpoint-deleted state retained.

## 3. Exact mixed clock transport with the actual underhistory

Use the independent coefficient C_h(R)=[Y^h]F_N^0(R,Y) and actual matrix
T of [the feedback theorem](actual_clock_feedback_normal_form.md).
For a crossing j at position r in its overbridge, increasing h_j by
one decreases n_(r-1) by one and increases n_r by one. At independent
primitive parameters the finite binomial recurrence gives

    C_(h+e_j)(R)=b_j(h,R) C_h(R),
    b_j=(t_r/t_(r-1))
          *(1-Q^(n_(r-1)))/(1-z_(r-1)Q^(n_(r-1)-1))
          *(1-z_rQ^(n_r))/(1-Q^(n_r+1)).              (9)

Use its cleared form if a displayed numerator or denominator vanishes.
Inside the monotone simplex the factorial denominators are units;
the original boundary support remains part of the statement. No cyclic
continuation across h=0,d is inferred from a zero-over-zero recurrence.

For S_h(R)=C_h(R Q^(T h)) define the primitive parameter shift

    Sigma_j R_i=R_i Q^(T_(ij)).

The ACTUAL transport is

    S_(h+e_j)(R)
       =b_j(h,R Q^(T(h+e_j))) S_h(Sigma_j R).         (10)

It is not multiplication of S_h at the old parameters by (9).
Equation (10) changes the other event endpoints, bridge parameters
and closure source exactly by the actual underclock column T_(.,j).
It follows by substituting RQ^(T(h+e_j)) in (9). Thus the joint
anchor/clock connection is the exact pullback of the independent
one, with all causal histories and negative self-clock shifts retained.
Its compatibility is an identity of the actual functions, not an
assumption that the a_j are independent physical clocks.

For a regular leading coefficient action S_0, this produces the
feedback term T^T partial_(log R)S_0 in clock stationarity, as derived
in the feedback note. The anchor equations obtained from (3) likewise
retain the macro endpoint Q^L. Those are necessary equations for a
regular stationary contribution; they do not determine its intersection
with the original relative source.

There is also a source-level affine mark which its exponentiated
classical equation alone cannot read. On a regular branch with
log P_h=N S+o(N), equation (2) has leading ratio
exp(2*pi*i X_i partial_(X_i)S). The original coefficient contour has
the stationary equation X_i partial_(X_i)S=1, since d/N tends to one.
But Q^d tends to one, so the bounded-degree leading q-equation retains
only exp(2*pi*i X_i partial_(X_i)S)=1. Its integer lift has to be fixed
by the original charge window and source, not by this equation alone.
The exact homogeneous alias theorem fixes that window on the WHOLE
finite coefficient; it does not authorize replacing every classical
integer branch by its required lift before the period is compared.

## 4. Why localization does not select the nilpotent source

The actual source algebra at its jet fiber is

    A_0=K[X_1,...,X_k]/(X_1^N,...,X_k^N).

Every positive-degree linear form, and hence every nonconstant D_i,
is nilpotent in A_0. Localizing A_0 by such a D_i gives the ZERO ring.
This follows directly from D_i^M=0: after adjoining its inverse one
gets 1=0. Therefore the rational connection R_i cannot simply be
restricted as an invertible connection to the original jet source.

The endpoint-deleted polynomial (6) is still a legitimate specified
lift in the ordinary ring. It is not determined by division of the
class of P_h in A_0, where D_i is a zero divisor. Keeping (6) is the
minimal extension needed by the actual cleared current (7).

There is an additional exact loss of data if the source is taken first.
The homogeneous degree-kd class is

    [P_h]=lambda(P_h) Omega,
    Omega=product_i X_i^d.

On this line tau_i acts as the constant Q^d, independent of L_e,
a_e and their macro limits. Also N_i[P_h]=D_i[P_h]=0 whenever their
degree is positive. Thus the geometric endpoint information in (3)
lives BEFORE the socle projection, in its stated factorized source
extension, not in a nontrivial localized connection on that one line.

Generic nonzero Fermat fibers avoid this localization problem and
have the exact same original period. But invertibility of P_h or of
its endpoints there does not imply that its specified Fourier/residue
coefficient is nonzero. The next actual example retains macro defects.

## 5. Actual hyperbolic-source sector with macro defects and zero period

Use the original figure-eight braid [1,-2,1,-2] and its actual clocks
h=(d,0,0,0). After the exact three closure contractions, write its four
remaining anchors as X_0,X_4,X_5,X_6. Up to the retained NONZERO scalar,
its actual polynomial consists of the four full blocks

    B_d(X_5,X_0;Q),
    B_d(X_6,X_0;q^(N+3)),
    B_d(X_5,X_4;q^(N+1)),
    B_d(X_0,X_6;q^(N-1)).                           (11)

Its incidence defects S_i-2d are +d at X_0, -d at X_4 and zero at
X_5,X_6. Thus this test does NOT assume small or vanishing defects.

Its original selected coefficient is zero for EVERY N. The first full
block contracts X_5=X_0. The third then contracts X_0=xX_4, since
q^(N+1)Q^(-1)=x. The other two become B_d(X_6,X_4;Q) and a nonzero
scalar times B_d(X_4,X_6;1). Contracting the first gives X_6=X_4;
the remaining block contains X_4-X_4 and is zero. Every contraction
is the actual arbitrary-exterior source identity, with its scalar
retained. No bare geometric quotient or unknown knot period is used.
This is also a special case of the separately proved first-cut clock
support in [the alternating-source theorem](actual_alternating_balanced_source.md);
the contraction above is included as a diagnostic of the connection,
not as a new knot-specific selection mechanism.

Nevertheless the polynomial in (11) is nonzero in the ordinary ring.
Choose generic independent nonzero Fermat centers so that
C_u!=a_e^N C_v for every edge. Then ALL its factors, endpoint
denominators and P_h itself are units on that semisimple fiber. Its
flat rank-one connection (5), actual T feedback and original source
currents remain exact, while its selected period is still zero by
center independence of the original homogeneous source.

This is not a counterexample to a geometric-sector theorem: the full
knot sum has other clocks, and no geometric contribution is claimed
for (11). It proves that a nonzero actual section, a regular flat
bounded-degree connection, source Ward equations and retained macro
defects do not ALONE force nonzero source projection.

## 6. Critical-path conclusion

The endpoint connection and mixed clock transport are exact tools for
the ORIGINAL state, with bounded endpoint complexity and full macro
coefficients. They do not yet prove anything stronger about geometric
selection than the previously known regular critical correspondence.
In particular there is no new broad-class volume lower bound here.

A successful further argument must preserve the endpoint extension
(6)-(8), the clock windows and T transport (10), and compute a nonzero
projection of their WHOLE original relative class to the marked
geometric branch. Specializing or localizing the socle first destroys
precisely the data which that comparison needs. The example (11)
prevents replacing the missing computation by rank-one flatness.

[Audit](../experiments/audit_actual_charged_connection.py) checks the
actual endpoint identities and source currents, original primitive
clock recurrences and feedback, and the all-N macro-defect source
annihilation (11). No literature proof is used as a premise.
