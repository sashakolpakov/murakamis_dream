# Pointed descent on the central Kashaev fiber

Research note, 25 October 2026. This supplies a nonzero meridian anchor
for the actual literature state and uses it to remove the central
comparison ambiguity on the fiber containing the Kashaev evaluation.
It also gives a cofactor formula for that evaluation from a specified
quantum A-operator when its rational solution line has rank one.
It does not prove that rank hypothesis for every knot or establish
the regulator norm comparison.

The subsequent [all-level A-period theorem](all_level_a_period.md)
removes the rank and regular-orbit conditions from a different exact
presentation. It uses cross-level polynomial rigidity, finitely many
fixed small colors, and uniformly bounded q-jets. The
[meridian-jet theorem](bounded_meridian_jets.md) gives the corresponding
integral-kernel bound without assuming rank one.

All conventions and the literature state are those independently
fixed in [the ADO pointing note](kashaev_ado_pointing.md). The torsor
and classical target remain those of
[the primary A-polynomial formulation](a_polynomial_torsor_status.md).

## 1. An anchor at the trivial quotient color

Fix N>=2, q=exp(pi*i/N), and use M=-q^(alpha+1). The reduced
literature period F_N is Laurent polynomial in M. For every knot,

    F_N(-q)=1, F_N(1)=<K>_N.                         (1.1)

More generally, for 1<=j<=N,

    F_N(-q^j)=C_j(q),                                (1.2)

where C_j is the normalized reduced j-dimensional highest-weight
period, with unknot value one. It is the usual reduced colored-Jones
normalization already compared directly in the crossing note. Here
only fixed small j is needed to specify initial values; no Jones
asymptotic or literature comparison theorem is a premise.

### Direct filtered-linear-algebra proof

At alpha=j-1 the N-dimensional color has

    E v_a=[a]_q[j-a]_q v_(a-1), F v_a=v_(a+1),
    K v_a=q^(j-1-2a)v_a.

The subspace U=span(v_j,...,v_(N-1)) is invariant under E,F,K,H.
Its quotient W has dimension j and is exactly the standard j-color.
The finite R and its inverse preserve U on each individual input
strand and induce the usual R on the quotient. Terms of degree
at least j vanish there. The pivotal matrix preserves U as well.

The following elementary trace fact is the relevant functoriality.
Use a basis adapted to U and its quotient on each strand of a braid
whose closure is a knot. Along an underlying strand, a state that
has entered U cannot leave U, since the crossing factors preserve
the subspace. In the induced cut operator on W, the open strand
starts and ends in the quotient. Partial trace identifies the other
endpoints. The braid permutation is a single cycle, so every traced
state contributing to this quotient block stays in W throughout.
Thus the induced cut operator is precisely the cut operator with
all strands colored by W. This assertion would need modification
for a separate closed link component not attached to the cut.

The two pivotal conventions on W differ by epsilon_j=(-1)^(j-1):

    K^(1-N)=epsilon_j*K,
    theta_ADO=epsilon_j*q^((j^2-1)/2).

For a b-strand knot braid of writhe w, w and b-1 have the same
parity. The total convention factor is therefore
epsilon_j^(b-1-w)=1. This proves (1.2). In particular j=1 is the
trivial quotient and gives the anchor in (1.1).

For each fixed j, C_j(q) is analytic near q=1 and C_j(1)=1. This
also follows directly from the finite matrices: [k]_q! tends to k!,
R tends to the identity, the braid tends to its permutation, and
the cut trace of a one-cycle permutation is the identity. These
initial periods consequently have no level-dependent exponential
normalization.

The compatibility of integer colors and ADO is existing coverage;
Willetts, [2003.09854](https://arxiv.org/abs/2003.09854), states a
more extensive unification. Its completion and recursion theorems
are not used in the proof above.

## 2. Pointing kills the central scalar on the relevant fiber

Let sigma(M)=qM with q of order n, E=C(M), K=C(u), u=M^n.
If h and g span the same nonzero rational solution line, then

    g=c(u)h, c in K^*.                               (2.1)

Suppose h is regular at M_0, h(M_0)!=0, and the corresponding
germ of g is regular with g(M_0)=h(M_0). It follows that c is
regular at u_0=M_0^n and c(u_0)=1. At every other point of that
sigma-orbit where h is regular, g has the same value as h.

This is an exact central-fiber statement, not a uniform growth bound.
It permits arbitrarily level-dependent c; its value on this fiber
has already been fixed by the pointing.

For the literature state, n=2N and

    M_*=-q, M_+=1, M_* q^(N-1)=M_+,
    M_*^(2N)=M_+^(2N)=1.                             (2.2)

Thus a comparison within the same rational solution line, normalized
by the actual anchor F_N(M_*)=1, has no remaining central multiplier
at the Kashaev point.

### A sufficient operator condition for the solution line

Given a specified operator P and its cyclic module as in the
intrinsic norm-torsor note, assume the row kernel of H-1 has
dimension one over E. Then all rational solutions form a
one-dimensional K-vector space, provided one nonzero solution exists.

Indeed a solution h defines the E-linear pairing ell_h by
ell_h(T^j e)=sigma^j h. It satisfies ell_h(H-1)=0. Two such pairings
are E-proportional by the kernel hypothesis, so g=c(M)h. Their
compatibility with T gives sigma(c)=c, hence c belongs to K.
The hypothesis concerns geometric multiplicity one; it does not
require H to be semisimple. It must be checked for the actual operator.

### An explicit period generator from Hilbert 90

This criterion also constructs a rational period from the operator.
Write T=B*sigma on the cyclic module and choose a nonzero row w with
wH=w. On this row line define

    Gamma(w)=sigma(w)B^(-1)=a*w.

The identity sigma(H)=B^(-1)HB preserves the line, and
Gamma^n(w)=wH^(-1)=w, so Norm(a)=1. The explicit Hilbert-90 sum

    f(c)=sum_(j=0)^(n-1)
           [a*sigma(a)*...*sigma^(j-1)(a)]*sigma^j(c)

has a choice of c for which it is a unit and a*sigma(f)=f.
Consequently ell=f*w obeys sigma(ell)=ell B. Its first component
h is a nonzero rational solution of the original scalar operator.
Changing c or the row frame changes h only by a central factor.

Normalize on the specified root germs M_+(u)=u^(1/n),
M_*(u)=-q*u^(1/n). Then for the reduced state

    <K>_N=[h(M_+(u))/h(M_*(u))]_(u=1), n=2N,        (2.3)

with common zeros and poles canceled as a whole germ. This is the
explicit norm-torsor/Hilbert-90 version of the cofactor period below.
It does not require equating D_n with the classical A-polynomial.

The one-dimensional solution-line hypothesis cannot simply be
omitted. For even N, the equation (T^2-1)h=0 admits both h=1 and
g=1+c*(M^N+1). They have the same value one at M=-q, but their
values at M=1 differ by 2c. This is an abstract equation, not a knot
counterexample. It explains the need for either the verified line
hypothesis or the finite initial-value data in Section 6.

## 3. The full ADO state is anchored by a central residue

Write N_N(M)=d_N(M)F_N(M) and eta_N=i^(N+3), as before. At M_*
the full state has a pole, so one must not replace the anchor by
an undefined ordinary value. Instead

    (u-1)N_N(M)=eta_N*(M-M^(-1))*M^N*F_N(M),
    [(u-1)N_N]_(M=-q)=eta_N*(-1)^N*(q-q^(-1)).       (3.1)

The last quantity is nonzero. At M=1, by contrast, the whole full
period is regular and N_N(1)=eta_N*<K>_N/N. The same central fiber
therefore requires different meridian frames at its two marked points.

To verify the residue, M_*^N=(-1)^(N+1) and
M_*-M_*^(-1)=-(q-q^(-1)). Equation (1.1) then gives (3.1).
If a rational comparison of full states preserves this residue,
(2.1) again gives c(1)=1. It therefore preserves the regular full
state value at M=1, and hence the Kashaev value. This is the same
pointed descent with its actual peripheral lattice.

## 4. The root period can be read from the quantum A-operator

Let P(q,M,T) be a specified reduced-state annihilator. At q=q_N,
view it as a K-linear operator on E, using

    E=K[M]/(M^n-u), n=2N,
    basis 1,M,...,M^(n-1),
    X=multiplication by M, S=diag(1,q,...,q^(n-1)),
    A_n(u)=sum_j a_j(q_N,X)S^j.                       (4.1)

This is an n by n matrix over K. Assume its generic nullity is one.
It is a direct checkable condition on the given root-level A-module.
Then its kernel is exactly K*F_N, since F_N is a nonzero solution.

Work over the DVR O=C[u]_(u-1). The integral period lattice

    Lambda=ker_K(A_n) intersection O^n

is free of rank one and saturated in O^n. The Laurent polynomial
F_N is in this lattice and is primitive because F_N(M_*)=1.
For any primitive generator w of Lambda, let

    e_+=(1,1,...,1), e_*=(1,M_*,...,M_*^(n-1)).

The denominator e_* w(1) is nonzero and

    <K>_N=e_+ w(1)/(e_* w(1)).                       (4.2)

This is the period pairing on a pointed projective kernel line.
It contains no free normalization scalar.

Clear rational denominators of A_n by a central scalar and choose
any nonzero column w_raw of its adjugate. Generically its rank is
n-1, so such a column spans the kernel. Divide out the common
(u-1)-valuation to obtain w. Equivalently compute

    <K>_N=[(e_+ w_raw(u))/(e_* w_raw(u))]_(u=1),       (4.3)

as a whole central germ. This remains valid if all the displayed
cofactors vanish at u=1 and the specialized matrix has a larger
kernel. The saturated generic line, rather than the whole enlarged
special kernel, specifies the period. A different nonzero column,
or a central clearing denominator, gives the same ratio.

The construction also applies to a specified finite system of
annihilators, hence to the joint kernel of generators of a quantum
A-ideal. If that joint kernel has dimension one, choose n-1
independent rows from the stacked matrix and take their signed
maximal minors. They give the same projective kernel line and the
same pointed ratio. Independence of the row choice follows from
uniqueness of a one-dimensional kernel. No arbitrary favorable
generator of an ideal is being substituted for the actual system.

## 5. The full-state formula retains one meridian jet

The actual reduced/full gauge is multiplication by the nonzero
rational function d_N over E. It is a K-linear isomorphism, so the
generic rational kernel dimensions in these two normalizations
agree. Their integral frames at u=1 differ, which is why the full
state requires the jet below.

For a full-state annihilator with generic rational nullity one,
its integral kernel is generated by the primitive vector for
R_N=(u-1)N_N. At M=1 this vector has zero evaluation. Its first
meridian jet, rather than that zero value, gives the full state.

Choose the root M_+(u)=u^(1/n) with value one, and
M_*(u)=-q*u^(1/n). Let e_+(u),e_*(u) be their evaluation rows in
the monomial basis. For a primitive generator w,

    j_+(w)=sum_(j=0)^(n-1)[w_j'(1)+(j/n)w_j(1)],
    <K>_N=N*(-1)^N*(q-q^(-1))*j_+(w)/(e_* w(1)).      (5.1)

This follows by differentiating R_N(M_+(u))=(u-1)N_N(M_+(u))
and using the nonzero residue (3.1) to fix the scalar at u=1.
A derivative of that scalar does not contribute, since e_+w(1)=0.

For any nonzero adjugate column the equivalent whole-germ formula is

    <K>_N=N*(-1)^N*(q-q^(-1))*
      [ e_+(u)w_raw(u) / ((u-1)e_*(u)w_raw(u)) ]_(u=1). (5.2)

The specified root germs are essential here. Equations (4.3) and
(5.2) give the same period under the actual reduced/full ADO gauge.
This explains precisely where a first jet and the peripheral factor
enter an intrinsic A-operator formulation.

## 6. A finite initial-value presentation when the orbit is regular

There is another exact presentation that does not require a
one-dimensional rational solution space. Suppose the scalar operator
has order d and its coefficients and forward companion matrix are
regular at the orbit points M_j=-q^j, j=1,...,N-d, with nonzero leading
coefficient there. The equation propagates the initial vector

    (F_N(M_1),...,F_N(M_d))=(C_1(q),...,C_d(q))        (6.1)

to F_N(M_N)=<K>_N by its ordered companion product. For fixed d the
initial periods are the analytic, level-independent functions of q
in Section 1. The quantum A-equation and this finite pointing specify
the exact period on that orbit. At singular orbit points the stated
propagation argument cannot simply divide by a vanishing coefficient;
the integral lattice or additional compatibility must be retained.

The subsequent all-level theorem supplies this compatibility from
the actual integer-color identities. It first propagates rational
functions in q and then evaluates the whole q-germ at q_N. Its jet
bound is D(s-1), with D the leading M-span and s its support size;
it does not assume the fixed-q meridian jets are bounded.

## 7. Remaining volume theorem

Under the hypotheses of Section 4, (4.3) is an A-operator-only
formula for the actual literature period. Consequently the requested
volume conjecture is exactly the assertion that this pointed
cofactor ratio has logarithmic growth Vol(S^3 minus K)/(2pi).
No replacement invariant is being defined by a favorable quantization.

This is not a proof of that growth statement. A nonzero actual
all-level knot operator is now supplied by the
[finite cut-state argument](finite_sum_annihilator.md). Its geometric
classical symbol and comparison of the pointed period with the
marked regulator still require proof in the desired knot class.
Solution-rank and orbit-regularity conditions remain hypotheses of
the particular formulas above; the all-level whole-germ presentation
no longer needs them.
The reference anchor removes the residual central normalization
once the comparison line has been identified; it does not identify
a geometric period with that line by itself.

The independent checks in `experiments/audit_root_orbit_pointing.py`
compare full and quotient colors directly and test the cofactor and
lattice prescription, including a fiber where the matrix rank drops.
They supplement the uniform arguments above.
