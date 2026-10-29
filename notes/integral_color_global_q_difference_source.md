# The actual integral-color path has a global polynomial q-difference model

Research proof, 27 October 2026. Along the simultaneous path
q_lambda=exp(pi*i lambda/N), M=-q_lambda^N, the finite head is a
genuine integral-color quotient for every parameter. Its standard
q-polynomial operators patch on O(N-1), with removable q=1 values.
There is also an explicit regular frame for the original balanced
source and all its crossing matrices along the entire closed path.

The source, cup, cap and pivot changes are recorded. The standard
ordinary closure gives the existing reduced color C_N(q); the
literal auxiliary pivot gives the earlier auxiliary word with its
known off-root route adapter. They agree at both endpoints but
are not silently identified in the interior.

Use [the common-Verma quotient](common_verma_two_wall_source.md) and
[the divided-color/pivot calculation](complete_color_divided_ward_and_fusion.md).
The independent [ordinary-frame symbol audit](integral_color_coherent_symbols_and_uniform_poles.md)
and [factorial-frame analysis](quantum_factorial_frames_and_cyclotomic_source.md)
give complementary uniform symbol and frame estimates.

## 1. The simultaneous path stays on the genuine quotient wall

Put n=N-1, Q=q^2, rho=q-q^(-1), and

    q_lambda=exp(pi*i lambda/N),
    M_lambda=-q_lambda^N, 0<=lambda<=1.

Then

    w=M Q^(-N)-M^(-1)=0,
    delta=1-Q^N=1-exp(2pi*i lambda).                       (1.1)

The tail of the genuine balanced infinite module is invariant on
this wall. Its finite head is therefore a quotient for the whole
path. The truncated Hopf defect -delta*w*E_(n,n) vanishes identically;
there is no generic-M finite Hopf premise.

The endpoints are (q,M)=(1,-1) and (q_N,1). Both also have
delta=0. The two wall parameters have not been identified: this
path lies in w=0 and meets the root wall at its endpoints. Its
logarithmic derivative is the integral-color direction

    dLog M=N dLog q,

not the fixed-meridian q-normal derivative.

## 2. The integral color and the two polynomial frames

In the ordinary F-shift basis v_j, 0<=j<=n, the genuine color is

    K v_j=q^(n-2j)v_j,
    F v_j=v_(j+1),
    E v_j=[j]_q[N-j]_q v_(j-1),                           (2.1)

with both boundary arrows zero and [r]_q=(q^r-q^(-r))/rho.
Its matrices are Laurent regular at q=1 with [r]_1=r.

The user's ordinary-falling polynomial basis is

    e_j=v_j/(n)_j, (n)_j=n!/(n-j)!.

It gives exactly

    F e_j=(n-j)e_(j+1),
    E e_j=[j]_q[N-j]_q/(N-j)e_(j-1).                      (2.2)

On the polynomial space H_N=H^0(P1,O(n)), e_j=x^j, this is

    F=x(n-J), E=x^(-1)[J]_q[N-J]_q/(N-J),
    K=q^(n-2J), J=x partial_x.                            (2.3)

The inverse N-J is legitimate on this space: its eigenvalues are
1,...,N. Equivalently it is the finite polynomial operation
integral_0^1 t^(N-1)f(x/t)dt. Thus (2.3) is an exact operator on
H_N, including q=1. It is not claimed to be a scalar first-order
q-difference expression on unrestricted functions.

For a simpler q-difference realization, use symmetric q-falling
factorials

    [n]_q^(fall,j)=product_(r=0)^(j-1)[n-r]_q,
    f_j=v_j/[n]_q^(fall,j).

Then

    E f_j=[j]_q f_(j-1),
    F f_j=[n-j]_q f_(j+1).                                (2.4)

With the marked shift T_q f(x)=f(qx), these have the exact forms

    E_q=(T_q-T_(q^-1))/(rho x),
    F_q=x(q^n T_(q^-1)-q^(-n)T_q)/rho,
    K_q=q^n T_(q^-2).                                    (2.5)

The apparent x pole cancels on polynomials; the highest coefficient
of F_q is zero, so all three preserve degree <=n. Their q=1 values
are partial_x, x(n-J), I, respectively.

Along the entire path, for 1<=r<N,

    [r]_(q_lambda)=sin(pi lambda r/N)/sin(pi lambda/N)>0,

with value r at lambda=0. None of the q-falling frame factors
vanishes or has a pole. The ordinary-falling frame differs by

    e_j=R_j f_j,
    R_j=[n]_q^(fall,j)/(n)_j.                             (2.6)

These are units on the fixed-N path. This is not a uniform-in-N
norm assertion; the factorial-frame note records its possible
exponential conditioning.

## 3. The q-difference operators patch globally on O(n)

The south section of a north polynomial is

    (J_n f)(y)=y^n f(1/y).

Direct substitution into (2.5) gives

    J_n E_q J_n^(-1)=
        y(q^n T_(q^-1)-q^(-n)T_q)/rho,
    J_n F_q J_n^(-1)=(T_q-T_(q^-1))/(rho y),
    J_n K_q J_n^(-1)=q^(-n)T_(q^2).                       (3.1)

Thus E and F interchange and K inverts, in the same line-bundle
transition that defines O(n). The q=1 limits give its usual
global sl2 vector-field action. This is an exact globally patched
q-difference realization, not a substitution into a local symbol.

The frame R in (2.6) also patches by J_n R J_n^(-1); it need
not have a scalar first-order difference expression. For q!=1
on the given path, spectral interpolation in T_q expresses it
and its inverse as finite q-difference matrices. Coefficients of
that interpolation can have removable q=1 singularities even
though the operators themselves are regular.

The reciprocal polynomial chart J_n is not automatically the
previously fixed balanced physical Weyl/source matrix. Transporting
a specified such matrix C into the h frame below gives D^(-1)CD,
with all its original phases and source factors. The chart identities
(3.1) do not authorize replacing that transported matrix by J_n.

## 4. A regular frame keeps the actual balanced pointing

Let w_j be the original balanced common-Verma basis. Its exact
relation to (2.1) is

    v_j=(Q;Q)_j w_j,
    (Q;Q)_j=product_(r=1)^j(1-Q^r).                       (4.1)

For example along M=-q^N the balanced Ecal arrow is
-q^(-j)rho[N-j]_q, and multiplication by
1-Q^j=-q^j rho[j]_q proves (2.1), with E=Ecal/rho^2.
The factors in (4.1) have zeros at q=1. Treating (4.1) as an
invertible integral frame there would lose source information.

The correct regular balanced-to-polynomial frame is instead

    h_j=D_j w_j,
    D_j=(-1)^j q^(j(j+1)/2)/{n choose j}_q
       =(Q;Q)_j/[rho^j [n]_q^(fall,j)],                  (4.2)

where the binomial is the symmetric q-binomial. Its ratio is

    D_j/D_(j-1)=-q^j [j]_q/[N-j]_q.

Here D changes basis vectors, so its inverse conjugates old
coordinate matrices. The coordinate gauge in the
[independent source-detour audit](integral_color_source_detour_audit.md)
is exactly D^(-1), expressed using the ordinary Q-binomial.

All factors in (4.2) are nonzero analytic functions on the closed
path. Their endpoint values are

    D_j(0)=(-1)^j/binom(n,j),
    D_j(1)=(-1)^j q_N^(j(j+1)/2).                         (4.3)

For the second equation use [N-r]_(q_N)=[r]_(q_N), so
{N-1 choose j}_(q_N)=1. In particular the root frame is a unitary
diagonal phase in the original Euclidean basis.

In this regular frame the actual Gauss matrices are precisely

    Ecal= rho E_q, F= rho F_q, K=K_q.                     (4.4)

Both first operators are regular and vanish at q=1. The original
ordinary Uq generators are E=rho^(-1)E_q,F=rho F_q on this frame;
their individual lattice need not be regular at q=1. The ordinary
integral Uq lattice of (2.4) is regular there. These two lattice
statements must remain distinct.

Their braiding matrices agree nonetheless for q!=1: the common
Hopf rescaling of E and F cancels in every E^k tensor F^k term
of the actual universal finite-color crossing, and K and the
Cartan weights stay unchanged. Equivalently, the change from f_j
to h_j divides by rho^j on every leg, which commutes with each
crossing by exact total-index conservation. The finite crossing
and its inverse therefore extend regularly to the usual flip
at q=1 in this model. No divergent ordinary generator is inserted
into a limit without this cancellation.

### 4.1 Source, dual source, cup and cap

The prescribed balanced cut has psi_j=1 and phi_j=1/N. In the
regular frame (4.2) it is exactly

    psi_h,j=D_j^(-1), phi_h,j=D_j/N,
    Gamma_h,ij=D_j/(N D_i), phi_h psi_h=1.                (4.5)

These are regular at both endpoints. They are not silently
replaced by a constant vector and average covector. Their norms
need not be bounded uniformly in N; already D_j(0) contains
ordinary binomial factors.

The dual basis is transformed inversely. Consequently the exact
cup sum_j w_j tensor w_j^* equals sum_j h_j tensor h_j^*.
For either diagonal pivot g, the right cap has entries

    ev_g(h_j tensor h_k^*)=delta_(jk) g_j,

so the basis change preserves the cup/cap pair without a missing
determinant or endpoint multiplier. All source and co-source
normal derivatives follow by differentiating (4.2)--(4.5).

For an actual one-cut closed braid array, total integer index
conservation makes its remaining cut matrix diagonal, even before
using a Hopf or Schur argument. Therefore its exact scalar cut is

    phi_h C psi_h=(1/N)Tr C.                             (4.6)

This is why the same actual scalar is represented by the fixed
compact coherent trace period in the h frame. Equality (4.6)
does not identify all offdiagonal source operators or erase their
derivatives before the closed network has been formed.

## 5. The ordinary and literal auxiliary closures stay distinguished

The genuine ordinary pivotal closure uses K. With its original
ordinary zero-framing twist and finite-color normalization, (2.5)
gives exactly the existing reduced color C_N(q). For generic q
the one-cut ordinary operator is scalar by actual Hopf naturality
and irreducibility; the resulting Laurent period extends to the
whole path, including both endpoints. Its values are

    C_N(1)=1, C_N(q_N)=Kashaev_N.                         (5.1)

The root auxiliary construction uses K^(1-N). Away from q_N it
differs from the ordinary cap by the diagonal K^(-N), with entry

    q^[-Nn+2Nj].

Its associated twist also differs. The exact zero-framed b-strand
route adapter is the previously proved factor

    q^[Nn(ell-b+1)+2N sum_(closed legs)j_a],               (5.2)

where ell is writhe. It equals one at both q=1 and q=q_N because
ell=b-1 modulo two for a knot. Its interior values and derivatives
are generally state-dependent and are retained.

Thus (4.2) is a genuine unit frame for the same balanced auxiliary
pointing along the path. Identifying its literal-pivot scalar with
C_N(q) in the interior requires (5.2), not a basis argument.
For either specified closure, the new model preserves the entire
word and original scalar. Neither the full root modified-dimension
line nor an ordinary quantum dimension is declared an off-root
extension of the other by this construction.

## 6. Exact finite coherent symbols and uniform endpoint behavior

Use the fixed compact coherent kernel of dimension N, variables
v,z, and T=vz/(1+vz). Put

    B_+=1+(q-1)T, B_-=1+(q^(-1)-1)T.

Binomial summation of the actual matrices (4.4) gives exactly

    sigma_(Ecal)=[B_+^n-B_-^n]/v,
    sigma_F=v[q^n B_-^n-q^(-n)B_+^n],
    sigma_K=q^n[1+(q^(-2)-1)T]^n.                        (6.1)

The first numerator vanishes at T=0 and the bracket in the
second vanishes at T=1. Thus these are smooth entire-sphere
symbols in the actual coherent charts, including both poles.

For s=2pi*i lambda, q=exp(s/(2N)), their limits are

    e_s=2sinh(sT/2)/v,
    f_s=2v sinh(s(1-T)/2),
    k_s=exp[s(1/2-T)].                                   (6.2)

Convergence is O(1/N) in every fixed smooth derivative norm on
the real sphere, uniformly for lambda in [0,1]. To prove it,
expand n Log[1+(exp(epsilon*s/(2N))-1)T], epsilon=+1 or -1.
Its difference from epsilon*sT/2 and every fixed derivative is
O(1/N), uniformly on the
compact (lambda,T) rectangle. The endpoint zero factors may be
divided using the exact integral identities g(T)/T=integral_0^1
g'(uT)du and g(T)/(1-T)=-integral_0^1 g'(1-u(1-T))du.
These remove the apparent v or south-chart pole with the same
derivative bound. The kernel charts then give the stated whole-
sphere estimate. No such estimate is asserted for an arbitrary
growing full braid matrix.

These principal functions satisfy identically

    e_s f_s+k_s+k_s^(-1)=2cosh(s/2).                      (6.3)

They describe the same meridian conjugacy class as the simultaneous
path. At lambda=0 their multiplicative Gauss matrix is I. Its
first lambda derivative retains the nonzero ordinary sl2 moment
map; no dimension-N integral representation has disappeared.
At lambda=1 the trace is -2, with the marked central sign of the
original complete source.

The plus eigenflag has the particularly simple exact principal form

    h_+(v,T)=exp[s(1-T)/2]v.                              (6.4)

It is a clock-preserving canonical shear. For imaginary s and the
real compact sphere its multiplier has modulus one, so the shear
sends the very same sphere to itself. The root factorial-frame note
records its quadratic generator, the inverse eigenflag and the two
negative inverse-flag bubbles. This smoother plus flag does not
permit replacing the actual inverse-flag source or its endpoint
current by a different marking.

The uniform estimates above concern the generator symbols only.
The actual selected period has the exact nearby-root ladder
C_N(q_(N+k))=C_k(q_(N+k)); in particular it equals one at
lambda=N/(N+1). The independent source-detour audit proves its
dense ordinary-color bounds and the resulting necessary endpoint
nonuniformity. Those statements coexist with the fixed-N analytic
source and uniform generator limits; no uniform full-word saddle
amplitude is being inferred.

## 7. Exact gain and remaining scope

The actual integral-color family now has a whole fixed-space
q-difference realization with explicit global clutch. The balanced
pointing, cup and both cap choices can be transported through a
unit frame on the closed simultaneous path. The only singular
factorial change is displayed in (4.1), and its regular network
cancellation is proved rather than assumed. The scalar compact
trace remains the actual one for every specified closure.

This does not remove the off-root pivot adapter, compare the full
root-normal source with a fixed-meridian q-jet, or bound the
unknown full-word norm in (6.1). Nor does it construct a global
geometric A-branch through the whole path or identify its selected
regulator phase. It supplies an actual globally patched family
on which those further comparisons can be posed with all source
factors visible.

The [exact audit](../experiments/audit_integral_color_global_q_difference_source.py)
checks the bases, matrices, global patch, true source/cup, actual
crossing cancellation, both walls, and endpoint symbols. The
[independent proof audit](integral_color_source_detour_audit.md)
also verifies the integral quotient, source frames, pivotal distinction
and exact resonance sampling constraints.
