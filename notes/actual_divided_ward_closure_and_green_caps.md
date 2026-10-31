# Actual divided Ward closure keeps a whole Green cap current

Research proof, 27 October 2026. Actual pivotal closure gives a
global current map for every finite weighted braid word and every
integral divided generator. The map retains the actual coupling
moments, the marked cut row, and the whole ordinary/frozen pivot
adapter. Its endpoint is an explicit inserted current, rather than
an inference from scalarity of the unweighted knot matrix.

This does not identify the resulting finite current with the two
internal geometric Gaussian currents. In particular the
[memory-Borel wall](degree_elevation_complement_bockstein_wall.md)
is not declared to be a quantum-group coproduct generator.
The high-color statements also do not identify its whole normal
jets with those of the original low color; only the previously
proved root scalar comparison may be used for that purpose.

## 1. The actual divided coproduct and adjoint

Use the generic integral Weyl family and the conventions

    Delta E=E tensor K+1 tensor E,
    Delta F=F tensor 1+K^(-1) tensor F,
    K E K^(-1)=Q E, K F K^(-1)=Q^(-1) F,
    S(E)=-E K^(-1), S(F)=-K F, Q=q^2.

Put E^(a)=E^a/[a]_q! and F^(a)=F^a/[a]_q!. Their matrices
are integral Gaussian matrices on every actual integral color.
They are retained before root specialization. Direct expansion of
the two q-commuting summands gives

    Delta E^(n)=sum_(k=0)^n q^(k(n-k))
                       E^(n-k) tensor E^(k) K^(n-k),
    Delta F^(n)=sum_(k=0)^n q^(-k(n-k))
                       K^(-k) F^(n-k) tensor F^(k).       (1.1)

For example AB=Q BA for A=E tensor K, B=1 tensor E.
The coefficient of B^k A^(n-k) is the ordinary Q-Gaussian;
dividing by [n]_q! changes it to q^(k(n-k)). This proves
(1.1) without a root-level division. Iteration retains every
multiindex of total size n, including mixed ordinary/divided terms.

The adjoint on matrices is A_h(C)=sum h_1 C S(h_2). In particular

    A_(E^(n))(C)=sum_(k=0)^n (-1)^k q^(-k(n-1))
                         E^(n-k) C E^(k) K^(-n),
    A_(F^(n))(C)=sum_(k=0)^n (-1)^k q^(k(n-1))
                         F^(n-k) K^(-k) C K^k F^(k).    (1.2)

The antipode factors in (1.2) follow by multiplying
S(E)=-E K^(-1) and S(F)=-KF. At n=N the terms 1<=k<N
are essential. Replacing (1.2) by a plain commutator with the
individual divided matrix loses them, even when that individual
matrix vanishes on a small color.

Write D_h=A_h-epsilon(h)I. All matrices in (1.1)--(1.2) and
their actual normal coefficients are regular on the integral
color lattice. Full Cartan, framing and peripheral scalar factors
remain part of every operator below.

## 2. An explicit integral current for every actual crossing

Write either signed actual checked crossing, with its literal
unwrapped transfer, as

    R_t(w)=sum_(k>=0) w^k R_(t,k), R_t(1)=R_t.

The sum is finite. The color list is switched after the crossing;
rho_in and rho_out denote its actual iterated coproduct matrices.
For any integral h define

    Xi_(h,t,k)=rho_out(h) R_(t,k)-R_(t,k) rho_in(h),
    J_(h,t)(w)=sum_(k>=1) (1+w+...+w^(k-1)) Xi_(h,t,k).

Actual R intertwining says sum_k Xi_(h,t,k)=0. Therefore

    rho_out(h)R_t(w)-R_t(w)rho_in(h)
                         =(w-1)J_(h,t)(w).              (2.1)

This is an explicit polynomial division by w-1. It neither
divides by [N]_q! nor chooses a root primitive. Hence it applies
directly to h=E^(N),F^(N) with (1.1), to both crossing signs,
and to every whole normal jet. Every transfer endpoint is present.
For h=E,F it is the generating transform of the literal
[crossing-transfer currents](local_r_ward_transfer_currents.md).

The same construction applies to a cut or component-position
weight w^J: its value at w=1 is the identity intertwiner. For a
link retain one such initial-position weight per component.

Let W(w)=R_m(w_m)...R_1(w_1), including any position weights as
additional factors. All actual tensor spectators are included in
rho_t(h). The elementary telescoping identity gives

    Xi_h(W)=sum_t (w_t-1) W_>t J_(h,t)(w_t) W_<t.       (2.2)

To pass to the true Hopf adjoint use the exact identity

    D_h(W)=sum_(h) Xi_(h_1)(W) rho_0(S h_2).

Thus (2.2) gives specified whole matrix currents B_(h,t) with

    D_h(W)=sum_t (w_t-1) B_(h,t)(w),
    B_(h,t)=sum_(h) W_>t J_(h_1,t)(w_t)
                                     W_<t rho_0(S h_2). (2.3)

All coproduct and antipode factors occur in their displayed order.
Equation (2.3) is a global finite-word current identity. It uses
actual matrices, rather than assigning a coproduct to the memory
Cartan or to a projected highest-spin corner.

## 3. The ordinary pivotal cap and its marked source row

For an actual closed tensor factor let

    P_o(C)=Tr_W[(I tensor K_W)C].

This is an exact intertwiner of the Hopf adjoints on ALL matrices:

    P_o D_h=D_h P_o.                                  (3.1)

For E the two internal terms cancel because K_W^(-1)K_W=I;
for F they cancel because K_W F_W K_W^(-1)=Q^(-1)F_W.
K is immediate by cyclicity. The identities extend to products;
alternatively (1.1)--(1.2) give a direct integral check for every
divided generator. Apply the generic identity first and then
specialize its regular matrices. This is the actual divided-cap
argument of [the marked-edge note](divided_adjoint_marked_edge_pairing.md),
now applied to the coupled currents (2.3).

Let Phi_A(C)=Tr(A C) be the original cut row, allowing its whole
q-dependent source, pivot and normalization. Its exact dual row is

    D_h^vee(A)=sum_(h) rho(S h_2) A rho(h_1)
                                             -epsilon(h)A.

Cyclicity, not invariance of A, gives

    Phi_A(D_h C)=Tr[D_h^vee(A) C].                     (3.2)

Consequently pivotal closure of (2.3) is the source-sensitive map

    Tr[D_h^vee(A) P_o W]
             =sum_t(w_t-1) Phi_A(P_o B_(h,t)).         (3.3)

The original coherent cut, uniform interval cut and normalized
trace are distinct A's in (3.2)--(3.3). They may not be substituted
for each other on the wall. In particular their values on the
normalized Frobenius wall E_(N,0) remain respectively 2^(-N),
1/(N+1), and zero.

## 4. Actual Green moments leave a finite difference of the moment

Put E_t=w_t partial_(w_t) and let p be any actual index-moment
polynomial. Define its forward finite difference by

    Delta_t p(x)=p(x+e_t)-p(x).

Apply p(E) to (3.3) and only then put every w=1. The exact product
rule p(E)(w_t f)=w_t p(E+e_t)f proves

    Tr[D_h^vee(A) P_o p(E)W]_(w=1)
          =sum_t Phi_A[P_o (Delta_t p)(E) B_(h,t)]_(w=1).
                                                               (4.1)

Thus a constant moment has zero current endpoint. A nonconstant
Green moment has the SPECIFIED lower-moment current on the right;
unweighted Schur scalarity does not make it zero. The identity
applies to every ordered binomial moment in the
[full finite Green certificate](full_certificate_framing_boundary.md).
It retains shifted supports because it was proved for the whole
coupled finite word before evaluating the couplings.

Equations (2.3), (3.2) and (4.1) give a literal current/source map
for arbitrary braids. Their coefficientwise normal derivatives
are full Leibniz convolutions, including derivatives of A, the
generators, every R, and the pivotal cap. The
[strict relative word transport](relative_word_green_transport.md)
carries these same whole identities and their marked endpoints
to its relative/Fock/Mellin/Rees diagram. It cannot turn the
right side of (4.1) into zero by omitting the endpoint row.

## 5. The frozen pivot has an exact whole moment-clock adapter

On an actual integral color of highest weight m and number J,

    K=q^m Q^(-J), Z=Q^N, chi=q^(Nm),
    g_f=K^(1-N)=chi^(-1) K Z^J.

Hence its WHOLE pivotal cap is

    P_f=chi^(-1) P_o M_(Z^J),                         (5.1)

where M means left multiplication on the CLOSED factor. This
is the literal position clock already included among the actual
Green/Jackson observables. It is not replaced by its root value.
For several closed factors use the product of their marked chi's
and clocks. The scalar chi and the external modified dimension
are retained exactly.

For a general diagonal g commuting K, direct expansion gives

    (P_g A_E-A_E P_g)(C)
       =Tr_W([K_W^(-1)g,E_W] C) K_V^(-1),
    (P_g A_F-A_F P_g)(C)
       =K_V^(-1)Tr_W[(gF_W-K_W F_W g K_W^(-1))C].      (5.2)

For g=g_f and delta=1-Q^N, the two cap rows are exactly

    [K^(-1)g_f,E]=(delta/(1-delta)) E K^(-N),
    g_f F-K F g_f K^(-1)=-delta Q^(-1) Fg_f.          (5.3)

They vanish at the root, but their first normal rows generally
do not. Formula (5.1) supplies the analogous ALL-divided answer
without division by delta:

    R_h:=P_f A_h-A_h P_f
       =chi^(-1)P_o[M_(Z^J),A_h].                    (5.4)

At the root Z=1, R_(h,0)=0 for every actual divided h. If a
subscript 1 denotes the delta coefficient, then

    R_(h,1)=-chi_0^(-1) P_(o,0)[M_J,A_(h,0)].        (5.5)

No derivatives of A_h have disappeared by assumption: their
commutators with M_(Z^J)|_0=I vanish identically. The root map
P_f,0=chi_0^(-1)P_o,0 has its full sign chi_0 retained.
Higher normal terms of (5.4) retain the binomial moments of
Z^J=(1-delta)^J and the generator/cap derivatives.

There is an exact ordered identity explaining why dividing a
small-generator cap row by the cyclotomic zero does NOT give a
nonzero root divided-cap defect. Write A=A_E on the full tensor,
a=A_E on the cut, R=P_f A-aP_f, and c_N=[N]_q!. Then

    sum_(j=0)^(N-1) a^(N-1-j) R A^j
         =P_f A^N-a^N P_f
         =c_N chi^(-1)P_o[M_(Z^J),A_(E^(N))].         (5.6)

The last side is divisible by delta*c_N, hence by delta^2.
All N ordered terms on the left must be combined BEFORE dividing
by c_N or delta. The same identity holds for F. Thus the root
frozen cap really commutes with the genuine divided adjoint,
whereas its first normal defect is precisely (5.5).

For the frozen cap replace (3.3) by the exact identity

    Tr[D_h^vee(A) P_f W]
       =sum_t(w_t-1)Phi_A(P_f B_(h,t))-Phi_A(R_h W).    (5.7)

Its Green version replaces the last term by
-Phi_A[R_h p(E)W]|_(w=1), in addition to the explicit
Delta_t p currents in (4.1). This is the surviving cap/source
term when the ordinary and frozen pivotal routes are compared.

## 6. A genuine divided Cartan row contracts the cut wall explicitly

On high color r=N use the constant beta frame and the ACTUAL word

    H_Fr(q)=tau [E^(N)(q),F^(N)(q)],
    tau=(-1)^(Nr-1).

Its root individual-color matrix is h_cl tensor I_head. Its
coproduct is tau[Delta E^(N),Delta F^(N)], with every mixed term
of (1.1), rather than a primitive sum assigned to the memory clock.
Let P_w select the extreme Fr block (N,0), keeping ALL head entries.
When a cut functional is written after P_w, that selected block is
embedded back in its original matrix corner before evaluation.
There is an exact WHOLE contraction, not only a root formula.
Both divided matrices preserve the residue strings j=aN+s, so
H_Fr(q) is diagonal for every q. Write its actual diagonal entries
as H_(a,s)(q), and set

    Lambda_(s,t)(q)=H_(N,s)(q)-H_(0,t)(q).

These are specified rational functions obtained by two products
of the actual integral Gaussian arrows. All have root value -2N,
so each is a regular UNIT in the whole local coefficient ring at
q_N. For every cut matrix C,

    P_w C=Lambda^(-1) entrywise* P_w[H_Fr(q),C].        (6.0)

No unknown comparison section or normal jet is used to define
this inverse. It preserves the actual source row by replacing it
with the explicitly rescaled row

    Phi_w^sharp(X)=Phi_A(embed_w[
                  Lambda^(-1) entrywise* P_w X]).

Thus Phi_A(embed_w P_w C)=Phi_w^sharp([H_Fr(q),C])
as a WHOLE rational identity, including the original q-dependent
source and its full peripheral scalar. At the root it becomes

    P_w[H_Fr,0,C]=-2N P_w C.                          (6.1)

Thus for any chosen cut source row the explicit root cochain row
-Phi_A P_w/(2N) contracts its wall component through the ACTUAL
Cartan commutator. This does not replace the memory-Borel complex:
it uses the additional actual divided quantum-group word H_Fr.
In particular it does not assert that this row is already one of
the two partially contracted geometric framing currents.

There is a completely specified all-braid pivotal map for (6.1).
For ANY Hopf element h and any full matrix C, (3.1) and the
antipode identity give

    [rho_cut(h),P_o C]
           =sum_(h) P_o(D_(h_1) C) rho_cut(h_2).       (6.2)

Indeed sum D_(h_1)(C)rho(h_2)=[rho(h),C]. Apply (2.3) to each
h_1 in (6.2). With Phi_w^sharp, this transports the WHOLE wall
row of the closed weighted word through actual pivotal closure.
For h=H_Fr its root version is the explicit sum of

    -(w_t-1)/(2N) * Phi_A P_w[
              sum_(h) P_o B_(h_1,t) rho_cut(h_2)].     (6.3)

All coproduct/mixed terms and their source factors are retained.
For a moment insertion replace w_t-1 by the Delta_t p rule of
(4.1). For the frozen cap replace each P_oD term by
D P_f=P_fD-R, using (5.4); the resulting cap term in (6.3)
has the SAME explicit R row, not a new unspecified source.

The normal Cartan corrections cannot be suppressed. Write
H_Fr(q)=sum_i delta^i H_i and C(q)=sum_j delta^j C_j. The exact
coefficient identity is

    P_w C_j=-1/(2N) P_w(
           [H_Fr(q),C(q)]_j-sum_(i=1)^j[H_i,C_(j-i)]). (6.4)

In particular the first normal contains the explicit term
[H_1,C_0]. Derivatives of the chosen source are applied afterward
by their full convolution. Formula (6.4) is the expansion of the
WHOLE unit inverse (6.0), not a substitute for it. This is a
source-sensitive cut-chain contraction for every actual closed
word. If its original Green
current is not homogeneous or is not uninserted, (6.3)--(6.4)
specify its remaining endpoint instead of setting it to zero.

## 7. Bare wall trace and a nonzero actual closed return

At the root the actual high-color pivot is independent of the
Frobenius block. Therefore closing a BARE Fr wall w=E_(N,0)
gives Tr_Fr(w)=0. Returning insertions change this statement:

    Tr_Fr(e^N w)=Tr_Fr(w e^N)=N!.

Both factors are actual integral divided-source matrices. Such a
dressed trace may not be replaced by the trace of its wall factor.
Likewise the original open-cut row sees Phi_+(w)=2^(-N), even
though the ordinary trace kills it. The
[incidence/source calculation](degree_elevation_wall_residual_and_source_moments.md)
and [actual crossing example](degree_elevation_complement_bockstein_wall.md)
already fix these distinct rows and an actual local current that
reaches the wall. The mixed adjoint in (1.2), the weighted word
current in (2.3), and the cap clock in (5.1) specify which factors
must accompany it through a real closure.

There is also a nonzero PIVOTALLY CLOSED actual R coefficient,
uniformly for every N. Take r=N, m=N(N+1)-1, k=N^2, and use the
positive UNCHECKED universal R on two actual high colors. Insert
on the closed first leg the literal coupon

    B=E_(N,0)^Fr tensor P_(head,0).

Consider the open matrix entry from index 0 to k. The closed
trace has exactly one contributing matrix entry: R takes the
closed index k to 0 with transfer k, and B returns it to k.
Writing eta_N=q_N^(1/2) with its marked phase, its first nonzero
normal coefficient is

    [delta^N] (ptr_K[(B tensor I)R])_(k,0)
       =q_N^(m-2k) N^N N! eta_N^(m(m-2k)) != 0.       (7.1)

All lower coefficients of this entry vanish. To prove it, use the
LITERAL transfer coefficient

    q^(k(k-1)/2) rho^k[k]_q! {m choose k}_q
                                             q^(m(m-2k)/2).

Its factorial part is (-1)^k q^(-k)(Q;Q)_k. For k=N^2 the
prefactor at the root is one. The N zero factors give N!delta^N,
and each of the N nonzero root blocks gives
product_(a=1)^(N-1)(1-Q_N^a)=N. Finally {m choose k}_(q_N)=1:
the ordinary Q-Gaussian cancels EXACTLY to the regular unit
product_(a=1)^(N-1)(1-Q^(N^2+a))/(1-Q^a), whose root value is
one, and the symmetric conversion factor is
q_N^(-N^2(N-1))=1. Multiplication by the CLOSED pivot at index k
gives (7.1). The frozen cap multiplies this leading coefficient
by its retained chi_0^(-1), so it is also nonzero.

Thus a bare wall has zero closed trace, but an actual universal
crossing can provide its return and yield a nonzero closed normal
source. This is a sourced R coefficient, not an assertion that an
uninserted knot has a nonzero wall. It also records why a fixed
normal-order test with order<N cannot see this particular return.

For the unweighted generic ordinary ribbon tangle, the complete
long matrix is scalar and its projected wall is zero. The stronger
usable statement here is the all-word formula (4.1): after a Green
insertion its exact defect is a finite difference of THAT moment,
with the source row still present. For the frozen ADO route add
the explicit whole cap clock (5.7). These are finite formulas to
check on a proposed geometric source map, not grounds for dropping
the Green endpoints. Bare wall trace, full uninserted scalarity,
and a Green/current endpoint are three different operations.

The [independent cut-charge/tail audit](global_green_cut_tails_and_wall_transport_residual.md)
records an additional exact
restriction: an original charge-zero array and scalar Green moments
have a diagonal cut kernel termwise. Homogeneous actual Hopf
currents retain their integer charge, including divided mixed
terms and normal jets. A cut tail outside the finite color range
is retained by its endpoint row rather than folded into the head.
These facts exclude a direct unmatched extreme wall in their
stated charge range; they do not remove a returning wall or the
current/source terms in (4.1) and (5.7).

The remaining geometric comparison must transport these specified
rows and currents through the actual partial Gaussian contraction.
Neither a memory-Borel contraction nor scalarity of the completed
unweighted word supplies that map.

Exact audits: [script](../experiments/audit_actual_divided_ward_closure.py)
and [results](../experiments/actual_divided_ward_closure_results.json).
The cap, ordered-divided cancellation, actual Cartan unit and
closed-return proofs have a separate
[independent audit](global_green_cut_tails_and_wall_transport_residual.md).
