# Sourced telescoping: a geometric-support criterion and the endpoint obstruction

Research note, 27 October 2026. This audits the connection between the
[finite-array annihilator proof](finite_sum_annihilator.md) and the
[nonzero geometric normal block](actual_geometric_normal_period.md).
It proves a conditional geometric-support criterion, an interior
certificate lemma, and a precise obstruction to the naive integration
map. It does **not** prove that the actual selected finite-state operator
annihilates the geometric normal block.

## 1. Use the same auxiliary lift as the normal coefficient model

The auxiliary lift in the finite-array proof takes the `(0,0)` entry of
the off-root cut partial trace. The normal coefficient model instead
uses the balanced constant vector and normalized-average covector. At
the root these give the same reduced scalar by scalarity of the actual
cut endomorphism. Off the root they need not agree, and their summands
have different supports.

For the present comparison use the off-root normalized-average lift

    Fbar_N(q,x)=(1/N) sum_(a=0)^(N-1) C_N(q,x)_(a,a),

in the same factorial boundary frame as the normal model. The gauge is
diagonal and invertible over generic `(q,x)`, so diagonal cut entries
are unchanged by it. At the actual root `Fbar_N=F_N`. Every crossing,
pivot and residual framing factor is retained. The common factor `1/N`
is independent of all shifts used in the finite-span argument, so it
does not affect that argument or any summand shift ratio.

This lift has a full-dimensional interior in the `d=m+1` independent
flow coordinates. Indeed, close strands `1,...,b-1` using the integral
cofactor of the knot permutation, with determinant `+1` or `-1`. The
initial positions are integral linear functions of the free cut position
`a_0` and the `m` transfers. Put `a_0=N/2+O(1)` and every transfer near
`epsilon*N`, with `epsilon>0` fixed and sufficiently small. At zero
transfer all positions equal `a_0`. Hence all positions on the fixed
word are `N/2+O(epsilon*N)`. Every transfer is positive, and all upper
position and transfer inequalities are strict for sufficiently small
`epsilon`. Small independent variations of all `m+1` coordinates
preserve these strict inequalities. Thus the support contains the
integer points in a nonempty open rational cone for large `N`.

The old cut-zero lift need not have this property. For example, one
positive two-strand crossing with cut position `a_0=0` has update
`(a_0,a_1)->(a_1+k,a_0-k)`. Closing the second strand forces `a_1=-k`;
nonnegativity then forces `a_1=k=0`. Consequently its summand array
cannot silently replace the full normal flow array.

## 2. A global array certificate restricts to an interior rational identity

Let `I_N(q,x;k)` be one of these proper, aligned summands and let

    P(x,z,T,S) I=0,       z=q^N,

be a global zero-extended certificate from the finite-span proof.
For each fixed shift occurring in `P`, choose a smaller open cone in
the interior from Section 1. For all sufficiently large integer points
of this cone, every shifted term in `P` remains supported. Divide there
by the nonzero reference summand. Proper alignment makes the result a
rational function

    R(q,x,z,t_1,...,t_d),       t_i=q^(k_i).

Then `R=0` as a rational function in the independent variables.

Here is the needed density argument. Clear the fixed rational
denominator, then expand the numerator as a finite Laurent polynomial
in `(q,x,z,t)`. If it is nonzero, precombine equal monomials and choose
an integer point `(N,k)` in the open cone avoiding every affine
hyperplane

    e-e' +(c-c')N +(alpha-alpha') dot k=0

arising from two distinct `(q,z,t)` exponent vectors. Such an integer
point exists: an open rational cone contains arbitrarily large lattice
boxes, while finitely many proper affine hyperplanes cannot cover
them. Distinct exponent vectors then give distinct powers of `q`
after `z=q^N,t_i=q^(k_i)`. The resulting Laurent polynomial in `(q,x)`
cannot vanish, a contradiction. Thus the numerator was zero.

This result imports no summation or cycle. It says that the **same
global certificate** is an interior contiguity identity. Any formal
realization of the exact actual shift ratios therefore satisfies that
identity before its internal variables are pushed forward. In
particular the local exact ratios in the normal-period note may be
used; their half-step, pivot, residual framing and base factors may
not be omitted.

## 3. The safe order of central specialization and moment extraction

Clear denominators of the whole certificate, then divide its largest
common central factor `(z+1)^r`, obtaining `P0`. The generic fixed-`N`
array identity survives this division: `q^N+1` is a nonzero element of
the rational function field in generic `q`. Thus

    P0(x,q^N,T,S) I_N=0.

The finite summands are regular at `q_N=exp(pi*i/N)`; the crossing
denominators have indices below `N`. Specialization gives

    P1(x,T,S)=P0(x,-1,T,S),

which is nonzero as a fixed Ore polynomial and annihilates the root
array for all but finitely many levels. If several direct-sum summand
components are retained, use their common certificate throughout.

Now expand

    P1=sum_alpha A_alpha(x,T)(S-1)^alpha.

For a least nonzero total degree `h`, every nonzero `A_alpha` of degree
`h` annihilates the actual summed root period. This is the finite
moment argument: for `w_i=exp(v_i)`, translation of the entire finite
zero-extended array is exact and

    P1(x,T,exp(-v)) F_N(x,v)=0.

At degree `v^alpha`, all terms containing a positive moment of `F_N`
have a lower-degree coefficient of `P1`, hence are zero. The surviving
term is `(-1)^h A_alpha F_N(x,0)`.

This order is useful for a formal comparison: remove the central
factor of the **whole certificate**, specialize, then extract moments.
Dividing a central factor from an individual moment coefficient only
after specialization is not justified by a formal source defined
solely at `z=-1`.

## 4. Conditional geometric-support theorem

Suppose the actual root-specialized contiguity realization admits a
linear weighted formal sourced pushforward `I_v` with all of the
following properties:

1. `I_v(S_i f)=exp(-v_i) I_v(f)` for every internal shift appearing in
   `P1` and its iterates.
2. `I_v(Tf)=T I_v(f)`, and external scalar coefficients commute with
   `I_v`.
3. `Z(v)=I_v(I)` is regular as a formal power series in the independent
   `v_i` at zero, and `Z(0)` is nonzero.
4. The unweighted period has its marked geometric WKB form

       Z(0)=C(h) exp(S/h) a_0 (1+O(h)),  a_0!=0,

   with `h=Log q`, the retained base-only line `C(h)`, and the actual
   meridian-step ratio having leading value equal to the marked
   geometric longitude `L`. All character and full-peripheral gauges
   are included in that statement.

For regularity in item 3 one may use `exp(S/h)K((h))[[v]]`, allowing a
different finite negative `h` order in each coefficient of `v`; no
uniform lower bound in the `v` degree is needed.

Then **one of the actual all-level operators constructed in Section 3
has a nonzero classical symbol vanishing on the geometric A-curve**.

Proof: apply `I_v` to the interior certificate. Items 1 and 2 give

    P1(x,T,exp(-v)) Z(v)=0.

The same least-degree coefficient argument as for the finite sum gives
`A_alpha Z(0)=0`. Choose one nonzero such coefficient and divide only
its common scalar `(q-1)` valuation, obtaining `Ahat`. This division
preserves the actual all-level root annihilation and the formal
annihilation. Let `a_cl(x,L)` be the first nonzero classical symbol of
`Ahat`; clear its rational denominators if necessary. Leading WKB
order of `Ahat Z(0)=0`, with `a_0!=0`, gives

    a_cl(x,L_geom(x))=0.

On an irreducible geometric branch this says that its defining
geometric A-factor divides the cleared classical polynomial, in the
stated peripheral gauge. The operator came entirely from the actual
global certificate and finite moment extraction. No known A-factor
has been appended to it. This statement concerns that constructed
annihilator; it does not assert that every annihilator, or the
minimal operator, has that factor. A larger annihilator's symbol can
contain factors absent from the minimal one.

## 5. Why the current relative source does not supply the hypotheses

The existing [relative source realization](relative_framing_source_transgression.md)
constructs a literal finite boundary projector, natural for all finite
linear matrices. It does not identify its auxiliary relative coordinate
with the two internal Gaussian framing modes. Consequently its
coefficientwise naturality is not item 1 of Section 4.

The failure of the naive replacement can be written exactly. At
completeness write

    Omega_cut=dt wedge beta,       beta=dlog A,

with marked endpoints `t=0,1`. On a relative top form the functional
is

    L(a,b_0,b_1)=integral_0^1 a(t)dt-b_1+b_0.

For any polynomial `f(t,A)`,

    L(partial_t f,0,0)=[f(1,A)-f(0,A)] beta.

It is generally nonzero. The relative coboundary is instead

    delta f=(partial_t f,f(0),f(1)),

and only this complete triple has zero transgression. Thus replacing
an internal summand divergence by an ordinary derivative on the
geometric framing chart loses precisely the endpoint co-source.

The finite-difference statement is equally explicit. For
`S_eta f(t)=f(t+eta)` and

    J_v(f)=integral_0^1 exp(v*t/eta) f(t)dt,

one has

    J_v(S_eta f)=exp(-v) J_v(f)
      +exp(-v) [integral_1^(1+eta) exp(v*t/eta)f(t)dt
                  -integral_0^eta exp(v*t/eta)f(t)dt].

These endpoint series are well-defined coefficientwise for
polynomial `f`, expanding in `v` with Laurent coefficients in `eta`.
Already `f=1` contradicts the desired weighted covariance for the
fixed relative interval: `S_eta f=f` and `J_0(f)=1`, whereas covariance
would require `(1-exp(-v))J_v(f)=0`. The source endpoints must move or
be compensated. Ordinary formal Gaussian integration in the transverse
directions does not remove this defect.

There is a second exact obstruction to replacing finite source data by
ordinary functions before pushforward. In

    C_N=k[A,A^(-1)]/(A^N-1),

the prescribed canonical representative satisfies

    A f_tilde - (Af)_tilde = f_(N-1)(A^N-1).

For `f=A^(N-1)`, the actual cut gives `phi_N(Af)=phi_N(1)=1`, while
the naive geometric operation gives
`Res_(A=0) A^N dA/A=0`. The existing source comparison is linear,
with this carry retained; it is not a ring map. Local interior
contiguity identities do not encode that carry by themselves.

## 6. Exact remaining statement

A sufficient next result is an explicit chain map from the actual
whole internal finite contraction, with all endpoint/carry strata, to
the relative geometric Gaussian pushforward, which sends every
internal shift to its weighted source action and gives a nonzero
unweighted geometric period. Section 4 would then force a geometric
factor in a specifically constructed actual all-level annihilator.

At present the normal block is nonzero before the remaining source
pairing, and the literal finite relative source is nonzero in its own
resolution. The map between these two pushforwards has not been
constructed. The endpoint identity above is an explicit reason why
their separate nonvanishing and ordinary integration by parts cannot
substitute for it. No conclusion about the selected global geometric
cycle or its volume growth follows from this note.
