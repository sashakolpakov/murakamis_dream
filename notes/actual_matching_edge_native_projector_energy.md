# Native magnetic energy controls every completed projector jet

Follow-up: the [Plancherel and full folded profile](actual_matching_edge_magnetic_energy_profile.md)
computes the full folded norm rate at both parities, and the
[real shrinking-fold theorem](actual_matching_edge_shrinking_fold_native_energy.md)
extends it to every j/N tending to 1/2. These are native real norm
results; shared source contraction and global geometric selection remain open.

30 October 2026. The completed target
operators in the [matching-edge block](actual_matching_edge_completed_projector_block.md)
have no additional exponential cost in any fixed generic-q derivative.
Their cost is the explicit, original-basis magnetic energy below.
That energy itself can be exponentially large, already for an odd
simple channel. Consequently this is a quantitative source interface,
not a polynomial operator bound or a whole-network estimate.

## 1. The source and its exact generic high-degree adapter

Put N>=3, d=N-1, q0=exp(pi i/N), q=q0 exp(epsilon), Q=q^2. The balanced
ordinary highest-weight-d representation has the ACTUAL generators

    F|u>=(1-Q^(u+1))|u+1>,
    Ecal|u>=q^-N(1-Q^(N-u))|u-1>,
    K|u>=q^(d-2u)|u>.

Use Omega=F_tot Ecal_tot+q K_tot+q^-1 K_tot^-1, with the original
coproducts. Its degree-t matrix for 0<=t<=d is J_t(q) in the
[physical generic-jet theorem](actual_q_hahn_physical_generic_jet_bound.md).
Write its upper and lower entries a_r^+,a_r^- and its normalized
column C_m(q;t,0)=1, with eigenvalue

    lambda_m(q)=q^(2N-2m-1)+q^(-2N+2m+1), 0<=m<=t.

The high-degree adapter is exact BEFORE root specialization. Define

    W(q)|u>=q^(-Nu)|d-u>.

Direct substitution gives WF=Ecal W, WEcal=FW and WK=K^-1W.
The commutator Ecal F-F Ecal=(q-q^-1)(K-K^-1) then proves that
P(W tensor W) commutes with Omega. On degree t its coefficient is
the constant q^(-Nt). Hence, for 0<=k<=d,

    J_(2d-k)[d-k+r,d-k+s]=J_k[r,s]                 (1)

as GENERIC matrices. The constant cancels in conjugation. The same
identity follows by substituting u=d-k+r into the three explicit
diagonals of the actual matrix. Thus every generic jet, including
large-partner jets, obeys the translated low-degree identity. This
statement strengthens the earlier root-only high-degree comparison;
it does not differentiate that root-only formula.

## 2. The magnetic energy and the operator theorem

Choose a completed pair 0<=j<l=d-j. This is the target pair g=j,
g'=l, but the compiler's channel indices are reversed. Let Pi_m be
the generic projector with eigenvalue lambda_m above, and define

    Q_j=Pi_j+Pi_l,
    M_j=(Omega-lambda_j I)Q_j.                      (2)

Thus M_j is EXACTLY the target nilpotent operator in the preceding
block theorem, with its target-index convention. It is not a
spectral derivative substituted for a generic-q derivative.

For each j<=t<=d put f=C_j(q0;t,.). If t<l, let sigma_(t,j)=f^T f.
If t>=l, let sigma_(t,j)=f^T w, where w is the original divided
pair, equivalently the spectral derivative of the root forward
recurrence. Define

    E_(t,j)=||f||_2^2/|sigma_(t,j)|,
    E_j^full=[E_(d,j)^2+2 sum_(t=j)^(d-1) E_(t,j)^2]^(1/2). (3)

These are explicit nonzero bilinear measures, not a chosen positive
metric on the channels. With s_r=product_(k=1)^r 2sin(pi k/N) and
a_j=|1-Q0^(2j+1)|, their magnitudes are

    |sigma_(t,j)|=s_(t-j)s_(t+j+1)/(s_t^2 a_j), t<l,
    |sigma_(t,j)|=N s_(t-j)s_(t+j-d)/(s_t^2 a_j^2), t>=l. (4)

The root columns are the original finite q-Hahn sums. Thus (3),(4)
contain no undetermined projector or inverse-frame norm.
If their normalized logarithms have a uniform limiting profile,
the square sum in (3) takes a maximum over the ONE physical degree
of this operator. It is not a product of maxima over independent
local degrees. In a network the magnetic indices and degrees remain
shared along the actual wires; applying separate local maxima can
lose precisely that incidence. The energy may have an explicit
variational rate without being polynomial or subexponential.

For every fixed r>=0 there is a constant C_r, uniform over N and
all pairs, such that in the ORIGINAL physical Hilbert--Schmidt norm

    ||[epsilon^r]Q_j||_HS <= C_r N^(8(r+1)) E_j^full,
    ||[epsilon^r]M_j||_HS <= C_r N^(8r) E_j^full.    (5)

For the operator norm the same bounds hold with E_j^full replaced
by max_(j<=t<=d) E_(t,j), since the physical degree blocks are an
orthogonal direct sum. They retain all physical total degrees and
both members of every pair. On a complete degree
t>=l one has the stronger exact root identity

    M_j(q0)|_t=f f^T/sigma_(t,j),
    ||M_j(q0)|_t||_HS=||M_j(q0)|_t||op=E_(t,j).     (6)

On j<=t<l, Q_j is the ordinary simple projector, its two displayed
norms equal E_(t,j), and M_j vanishes identically even generically.
Below degree j both operators vanish. In particular E_j^full is
bounded by C||Q_j(q0)||_HS: on complete blocks use
M_j=(J_t-c_j)Q_j and the uniform bound for the entries and bandwidth
of J_t(q0); on the other blocks use the exact rank-one norm.
Thus (5) also bounds every generic jet by a polynomial times the
actual root cluster norm. It does not bound that root norm itself
by a polynomial.

For odd N and the simple midpoint m=d/2, replace (3) by the same
sum over t>=m, with

    |sigma_(t,m)|=N s_(t-m)^2/s_t^2.

Then its isolated projector obeys

    ||[epsilon^r]Pi_m||_HS <= C_r N^(8r) E_m^full,
    ||Pi_m(q0)||_HS=E_m^full.                       (7)

## 3. Generic dual measures and the proof

The actual generic matrix is not symmetric. Retain its symmetrizer

    G_0=1, G_u=product_(r=0)^(u-1) a_r^+/a_r^-,
    G=diag(G_u), GJ_t=J_t^T G.                     (8)

At the root G=I. For a generic simple node its left row is C_m^T G.
The continuant Christoffel--Darboux identity gives exactly

    C_m^T G C_m
      =C_m(q;t,t) product_(h!=m)(lambda_m-lambda_h)
                              /product_(r=0)^(t-1) a_r^-. (9)

One can derive (9) directly by subtracting the two tridiagonal
recurrences, multiplying by the weights (8), and telescoping. In
monic continuants it is P_t'(lambda_m)p_t(lambda_m)/product a_r^+a_r^-;
since p_t=C_m(t) product a_r^+, this is (9). The endpoint is the
original generic monomial

    C_m(q;t,t)=(-1)^m q^[dt-2Nm+m^2+m].

Suppose t>=l, and put delta=lambda_j-lambda_l. Define the units

    b_m=C_m(q;t,t) product_(h!=j,l)(lambda_m-lambda_h)
                              /product a_r^-,  m=j,l,
    R_m=C_m C_m^T G/b_m.                            (10)

Equations (9),(10) yield the exact generic identities

    Pi_j=R_j/delta, Pi_l=-R_l/delta,
    Q_j=(R_j-R_l)/delta, M_j=R_l.                   (11)

At the root both b_m equal sigma_(t,j). This follows either by
the double-node specialization of (9), or from
sigma=f^T w=C_j(t) product_(h!=j,l)(c_j-c_h)/product a_r^-.
It proves (6), including its sign. The identities are consistent
with the actual target gap being -delta.

Here are uniform bounds on a genuine generic disk. Choose the
constant c in rho=cN^-8 sufficiently small. The physical-jet
theorem gives, for BOTH m=j,l,

    |C_m(q;t,u)| <= C |f_u|, |epsilon|<=rho.        (12)

The same theorem bounds every original offdiagonal ratio, while
the endpoint monomial has exponent O(N^2). All other root node
differences in (10) have magnitude at least 16/N^2 and generic
derivative O(N). Their relative change is O(N^3 rho), and there
are at most N factors. Therefore

    ||G||<=C, |b_m/sigma|+|sigma/b_m|<=C,
    ||R_m||_HS<=C E_(t,j)                          (13)

throughout the disk. No separate exponential estimate of a
factorial product has entered (13); it is a RELATIVE unit bound.

The actual collision gap is

    delta=(q^s-q^-s)(q^N-q^-N), s=l-j.

On |epsilon|=rho its magnitude is at least c rho: its linear
coefficient has magnitude 4N sin(pi s/N)>=8, and the two explicit
factors have uniformly controlled relative variation. The analytic
completed projector therefore has norm at most C rho^-1 E_(t,j)
on that circle by (11). Its holomorphy also follows directly from
the coprime quadratic cluster factor of the full characteristic
polynomial. Cauchy's formula proves its bound in (5). The regular
identity M_j=R_l gives the better M exponent in (5).

For t<l use (9) without deleting a partner: its norm is a unit
relative to the nonzero simple sigma, so (12),(13) give the simple
projector bound directly. The odd midpoint is identical. Finally
(1) duplicates each low block except t=d. Orthogonality of the
physical degree spaces in the original Euclidean basis gives
exactly the square sum (3), proving (5),(7) for the whole pair.

## 4. The energy is genuinely exponential

The distinction in (5) is necessary. Take odd N=2m+1 and the simple
midpoint channel in degree t=m. Its normalized original highest
column has

    |f_u|=s_m/(s_u s_(m-u)), 0<=u<=m,
    |sigma|=N/s_m^2=1.

Consequently its projector norm is EXACTLY

    E_(m,m)=sum_(u=0)^m [s_m/(s_u s_(m-u))]^2.       (14)

This is a native physical operator norm, not a bound obtained by
discarding phases in a contraction. Let
J(x)=integral_0^x log(2sin(pi y))dy. Elementary endpoint-controlled
Riemann sums give log s_floor(Nx)=N J(x)+O(log N), uniformly on
[0,1/2]. Since J(1/2)=0, the largest summand in (14) occurs
asymptotically at u/N=1/4: the derivative of
-J(x)-J(1/2-x) is log cot(pi x). Bounding the sum between its
largest term and (m+1) times that term proves

    lim_(odd N) N^-1 log E_(m,m)
       =-4 J(1/4)=2 Catalan/pi=v8/(2pi)>0.          (15)

The integral identity follows directly by integrating the Fourier
series for log(2sin), or may be taken as the defining integral for
the constant. Thus no uniform polynomial bound for the native
projector norms in the preceding block theorem is possible.
The scalar target normalization has been removed exactly, and
generic derivatives now add only polynomial cost. The remaining
magnetic energy must still be handled by coherent sewing, a sharp
variational estimate, or a different justified inner product.

Audit: [actual generic projectors, dual measures and high blocks](../experiments/audit_actual_matching_edge_native_projector_energy.py).

The focused audit checks 54 original generic high-block identities,
12 full Chevalley/Casimir commutations, 819 original column four-jets,
161 generic dual norms, 78 actual residue four-jets, 39 completed
cluster three-jets, 83 simple projector four-jets and 39 exact
rank-one nilpotent blocks. Independent actual highest columns also
check the native energy normalization in (14). The finite energy
sequence through N=513 illustrates the proved limit (15); it is
not the proof of that limit or of the uniform estimates.

Primary-agent analytical review independently checked the actual
Chevalley commutator and high-degree adapter, generic dual measure,
collision sign M=R_l, relative unit and gap bounds, whole-degree
assembly and the exact Steinberg exponential rate. Independent
source review rederived the same normalizations, including the
double-node measure and both root-measure regimes, and freshly
replayed every focused audit count above. Both reviews passed.
Their scope is the displayed native-energy bounds and obstruction;
no graph-wide positive pairing or sharp volume estimate follows.
