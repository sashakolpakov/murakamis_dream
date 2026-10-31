# Exact top-cap mark transport for the original arbitrary-Casimir source

Unpublished workspace theorem, 31 October 2026. Root and coherent completed
full internal analytical/source and code reviews and independent fresh
finite replays; this is not external peer review. The result is an equality
of the ORIGINAL complete-color finite sources. It is not a termwise mark
transport for a LEFT/CROSS/RIGHT projection or a theorem about the maxima
of their absolute envelopes.

## 1. Statement with the permitted cuts fixed

Fix N>=3, d=N-1, q_N=exp(pi i/N), and one actual ordered 2k-strand
flat plat. At each original box insert ANY finite polynomial

    f_e(Omega) R_e^(epsilon_e), epsilon_e in {0,+1,-1},

in its original order, with the full physical crossing/Cartan scalar.
Keep all main colors equal to V_d, all original bottom cups, and all
original top caps except that the single unrestricted mark is placed
at one selected top pair r. Let S_r be that literal raw contraction.
The same fixed exterior framing line may multiply every S_r.

Then S_r=S_s for ANY two of the original top-cap positions. In
particular this holds for two permitted cuts on the same main component.
It also holds for different top-cap components when they carry this
SAME complete color and these exact source conventions; that stronger
statement is proved below, not inferred from half-twist independence.

Coefficients of the polynomials may depend on N and on arbitrary
spectral variables. All original Hermite data are retained: this is an
identity of full matrices, not a simple-node interpolation. The result
applies in particular to the full cleared resolvent numerator V_N(sigma)
at every real or complex sigma, including repeated spectral nodes.

## 2. A regular finite-dimensional lift, not a generic ADO normalization

Hold N fixed and introduce a variable q near q_N, on the original local
square-root branch for the Cartan factors. On the ordinary highest-weight
module of highest weight d use

    K v_a=q^(d-2a)v_a, F v_a=v_(a+1),
    E v_a=[a]_q[N-a]_q v_(a-1), 0<=a<=d.

Endpoints are zero. The literal finite universal R has summation indices
less than N; all factorial denominators [h]_q!, h<N, are units at q_N.
Its inverse, the actual duality matrices, and all finite Casimir
polynomials are therefore regular there. No denominator [N]_q is used
in a matrix entry.

For clarity the self-duality is regular too. In the standard basis set

    J(q)v_a=c_a(q)v_(d-a)^*,
    c_a(q)=(-1)^a q^(a(a-N)).                         (1)

Using S(F)=-KF and S(E)=-EK^(-1), the F equation is
c_(a+1)=-q^(-d+2a)c_a, and the E and K equations give the same
intertwiner. At q_N, c_a=q_N^(a^2), the actual complete-color
duality. Change to the literal balanced basis v_a/F_a(q),
F_a(q)=prod_(h=1)^a(1-q^(2h)); every F_a with a<N is a unit at q_N.
The actual cup and cap formulas are thus regular specializations of
these generic finite matrices, with the root pivot correction below.

Extend each fixed root polynomial f_e by keeping its coefficients fixed
and replacing Omega by the generic pair Casimir Omega(q). Retained
R_e^(epsilon_e) is extended by its ACTUAL finite universal crossing,
not by a guessed generic interpolation of its root Hermite polynomial.
These are Hopf intertwiners in the actual oriented/dual frames.

For the cleared numerator an explicit choice avoids any inverse:

    f_sigma(z)=[chi_N(sigma)-chi_N(z)]/(sigma-z),
    chi_N(z)=2 T_N(z/2)+2.                            (2)

Equation (2) is a polynomial in z and sigma. Only AFTER specializing
q=q_N use chi_N(Omega)=0 to identify it with V_N(sigma). No generic
meromorphic resolvent or cancellation at a repeated node is assumed.

This construction is an auxiliary finite-dimensional polynomial
specialization. It does not identify the generic standard pivot with
the genuine-q ADO pivot or assert an equality of their transverse jets.

## 3. Scalar open caps and one generic closed contraction

Use the standard generic pivot K and its actual oriented evaluation and
coevaluation. After the boxes and all top caps except r, the network is
a Hopf map from the unit object to V_d tensor V_d^* at that pair.
Through the explicit cup identification this is an endomorphism C_r(q)
of V_d commuting with the generators. It is scalar: K has distinct
weights generically, and the consecutive nonzero F arrows force all
diagonal entries equal. Write C_r(q)=a_r(q)I.

Equivalently the remaining two-head vector is a_r(q) times its ORIGINAL
cup. The scalar is regular at q_N: it is one matrix entry of the open
network in the regular frames just constructed. This argument needs no
ordinary quantum dimension at the root and introduces no new mark.

Close the last pair with the ordinary K-pivotal cap. The result is the
SAME fully closed tensor contraction Z(q), independent of which cap
was temporarily left open. The explicit trace of K is

    Tr_(V_d)K=sum_(a=0)^d q^(d-2a)=[N]_q,
    Z(q)=[N]_q a_r(q) for every r.                   (3)

The dual has the same trace, by reversing this finite weight sum.
For generic q, [N]_q is nonzero, so all a_r(q) agree. They are regular
at q_N, hence their equality specializes. The division in (3) occurs
ONLY generically; no zero quantum dimension is divided at the root.
This uses literal finite tensors and a finite weight sum, not an imported
modified-trace cyclicity or ambidexterity theorem.

## 4. Return to the exact root pivot and unrestricted mark

At q_N every main weight has parity d, so the ACTUAL pivot is

    g=K^(1-N)=(-1)^d K.                              (4)

In the flat-plat convention all bottom turns are left cups and all
ordinary top turns are right caps. The left cups are unchanged; each
of the k-1 ordinary top caps therefore acquires the SAME factor
(-1)^d relative to the K-pivotal network. This is independent of r.

The balanced source formulas are, with x_0=q_N^d and Q=q_N^2,

    p_(i,j)=N x_0^(-j) delta_(i+j,d),
    ell_(i,j)=x_0^j g_i/N delta_(i+j,d),
    m_(i,j)=x_0^j/N^2.                              (5)

The mark m is unrestricted. Equations (1) and

    F_a(q_N)F_(d-a)(q_N)=N(-1)^a Q^(a(a+1)/2)

give the cup and ordinary cap in (5) directly. The original rank-one
source e=psi phi, psi_a=1, phi_a=1/N, has Tr(e)=1, and its marked
insertion is D=g^(-1)e. Thus Tr(gDC)=Tr(eC), and DIRECTLY mp=1.
For the scalar open vector in section 3, the original marked evaluation
is consequently

    S_r=(-1)^(d(k-1)) a_r(q_N),                     (6)

with no additional N, quantum-dimension division or component-dependent
factor. All full Cartan factors and retained half twists were already
inside the same a_r. A fixed original framing/peripheral character
multiplies both sides of (6) equally.

This proves the stated equality for all permitted top caps, at either
parity and composite levels. If the one-cut modified normalization is
used, its complete-color factor i^(N+3)/N is the same on any such
complete-colored cut. Deformed unequal main colors, unrestricted moves
of the nonintertwining defect D, and generic-q ADO derivatives are NOT
asserted to satisfy this identity.

## 5. Consequences and the remaining cap question

The exact homogeneous face-source identity therefore gives equal marked
coefficients for the different original top-cap targets, for EVERY
choice of the full Casimir polynomials. In particular the full S_N(sigma)
is identical as a polynomial in all spectral variables. This is stronger
than merely equality of the final knot scalar at one twist vector.

### Corollary: a certificate at any permitted original top mark

Fix a width $k\geq2$, an original ordered $2k$-strand flat-plat skeleton
$D$, and fixed retained half twists $\epsilon_e\in\{0,\pm1\}$. Suppose
the endpoint permutation gives a knot and that, at some original top
mark $r$, the diagram has the actual labeled simple-white geometric
certificate and satisfies **all** hypotheses of at least one of these
proved full-source criteria:

- [complete-radius balance](general_complete_radius_balance_filling_volume.md);
- the [anchored shared-radius criterion](general_anchored_shared_radius_filling_volume.md);
- a [finite cover of the actual sectors](general_actual_sector_cover_filling_volume.md).

The protected faces, complete packing, target extraction, and any finite
shared-radius witnesses in the selected criterion are those for mark $r$.
Choose this mark and certificate once, independently of the quantum level
and filling vector. Then there is $T(D)<\infty$, with the chosen certificate
included in the fixed data, such that for every independently signed
integer vector $\mathbf p$ satisfying $|p_e|>T(D)$, fixed before
$N\to\infty$, and for **every** original top mark $s$,

$$
\lim_{N\to\infty}\frac{2\pi}{N}
 \log\left|K_N^{(s)}\bigl(K_D(\mathbf p)\bigr)\right|
 =\operatorname{Vol}\bigl(S^3\setminus K_D(\mathbf p)\bigr). \tag{7}
$$

Here the actual crossing powers are $n_e=\epsilon_e-2p_e$ and
$K_N^{(s)}$ uses the original full normalization, with only the permitted
top mark changed. There is no comparability condition on the magnitudes
of the independent twists. Both level parities and composite levels are
included. The volume is that of the same actual filled knot exterior;
no claim of exact bridge number $k$, a joint growing-twist/level limit,
or a threshold uniform in different diagrams is made.

**Proof.** Let $S_{N,r}(\boldsymbol\sigma)$ be the full marked numerator
with the polynomial coupons (2), without an extra retained $R$ factor.
Sections 1–4, applied with $\epsilon_e=0$, give the exact polynomial identity
$S_{N,r}=S_{N,s}$ for every $N$. The original Fourier/Hermite transform is
a linear functional of this full polynomial. Its sine factors, charge
weights and parity, Gaussian powers $n_e=\epsilon_e-2p_e$, and scalar
$q_N^{d^2\sum_e n_e/4}(-i)^R$ are the same for both marks. Apply that
same exact transform to the polynomial identity. Multiplying by the
same recorded final-diagram framing/component character and complete-color
normalization therefore gives $K_N^{(r)}=K_N^{(s)}$ at every level.
The retained half twist appears exactly once, through $n_e$ in this
Fourier description; the alternative direct coupon description retains
its actual $R_e^{\epsilon_e}$ as in section 1.

At mark $r$, the selected theorem supplies the full original invariant
limit and a threshold depending on its fixed geometric and finite
certificate data. The exact scalar equality transfers that conclusion
to each $s$, with the same filled topology and threshold. In particular,
we do not transport its all-CROSS summand or its remainder decomposition.
This proves (7).

The width-three [mark-dependence example](research_complete_balance_mark_dependence.md)
separates two sufficient tests on the same literal diagram: one mark
passes balance while another fails. With the present corollary the
successful test suffices for either marked evaluation. This does **not**
prove strict enlargement of the underlying unmarked knot classes, and
does not show that every original diagram has a successful mark.

The identity does NOT transport an individual cap window or a chosen
LEFT/CROSS/RIGHT term. Those row projections are not arbitrary Casimir
polynomials/intertwiners. Their absolute coefficient arrays, protected
targets, signed-incidence cycles and envelope maxima change with the
mark. Equality of the summed polynomial does not identify those maxima
or guarantee that a new mark has no residual cap. The earlier finite-
collar obstruction remains unchanged. A direct termwise mark-slide or
an absolute cancellation estimate still needs its own proof.

The source inputs are the [original all-coupon identity](actual_homogeneous_casimir_face_source.md),
[literal duality](relative_pivotal_duality.md), [turns and rank-one mark](quantum_bridge_cap_source.md),
and [root Casimir relation and regular highest-weight construction](actual_crossing_circle_source_and_filling.md).
The [mark-dependence example](research_complete_balance_mark_dependence.md)
is separate geometry. The sufficient applications use the existing
[complete-radius balance theorem](general_complete_radius_balance_filling_volume.md)
or [anchored shared-radius theorem](general_anchored_shared_radius_filling_volume.md).
The [finite-collar obstruction](research_double_protected_cap_finite_collar_obstruction.md)
is unchanged. No literature proof theorem is used here.

## 6. Internal review and finite verification

Root and coherent independently read the analytical transport proof and
audit code, including the regular polynomial lift, generic-only dimension
division, exact root pivot sign and unrestricted marked normalization.
Both independently replayed the final finite audit. Root and coherent
also checked the explicit section 5 certificate corollary against all
three linked full-source theorems and the original Fourier normalization. The preserved
[portable audit](../experiments/research_audit_arbitrary_casimir_top_mark_transport.py)
and its [results](../experiments/research_arbitrary_casimir_top_mark_transport_results.json)
check original physical coproduct matrices, complete divided-polynomial
numerators at sigma=-2,2,0,3, arbitrary Casimir polynomials, and the actual
positive and negative crossings. They verify the remaining two-head
vector entrywise against its scalar times the original cup before
comparing the original top marks.

The exact finite fixtures reproduce 34 cases (31 nonzero), 82 marked
contractions, 2092 scalar-cup entries, 21 same-component comparisons and
45 different-component comparisons. Compatible root fields and a
conservative int64 bound are checked explicitly. The portable workspace
replay reproduces the reviewed private JSON exactly. These fixtures
support the normalization; the general theorem is proved in sections
1–4. They are not an audit of generic-q derivatives, projected sectors,
absolute envelopes or an asymptotic assertion.
