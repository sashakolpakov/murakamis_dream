# Fixed-root Ward data do not admit a literal scalar formalization

Research note, 27 October 2026. This isolates an obstruction to one
proposed shortcut from the exact all-matrices Hopf-Ward diagram to the
geometric Gaussian period. It also specifies what a homological
perturbation argument would have to supply. The obstruction applies
to a fixed-root, composition-preserving formalization. It does not
rule out a linear source-compatible comparison in a larger all-level
category, and does not invalidate the partially summed support theorem.

## 1. The fixed-N action cannot become a nontrivial near-identity flow

Fix `N>=2`, a characteristic-zero cyclotomic coefficient field, and
the actual matrices. Since

    K^N=x^N I,

their conjugation action satisfies

    (ad_K)^N=I.                                  (1.1)

The same relation holds on every tensor Hopf-adjoint matrix space.

**Finite-order lemma.** Let `E` be a separated, complete, H-torsion-free
module in characteristic zero, with `N` invertible. If a continuous
endomorphism `U` satisfies

    U=I+O(H),       U^N=I,

then `U=I`.

Proof: if `U=I+H^s D mod H^(s+1)`, expansion of the fixed finite
power gives `U^N=I+N H^s D mod H^(s+1)`, hence `D=0`. Induction
and separatedness give the result. Equivalently the H-adic logarithm
exists and `N log U=0`.

Consequently a comparison preserving (1.1) cannot send the actual
fixed-N adjoint action to a regular operator with principal form

    U=I+H A(h_sl/2)+O(H^2)

and a nonzero conjugation field on a framing coefficient algebra.
The same applies to the two cut-stabilizer fields obtained from
actual Hopf-adjoint combinations in
[the finite Ward calculation](actual_borel_ward_cut_contraction.md).

If an equivariant linear map has only an invariant image, this
conclusion applies only on that image: `U` acts as identity there.
An invariant rank-one scalar quotient is therefore **not** excluded.
The obstruction concerns simultaneously retaining the full fixed-N
action and realizing its nontrivial classical framing transport on
that image.

## 2. All matrices cannot map multiplicatively into scalar symbols

Let `A_H` be an H-adically separated, H-torsion-free complete algebra
whose special fibre is an integral domain. Then `A_H` is a domain.
Indeed two nonzero elements have finite H-valuations, and the product
of their first nonzero symbols cannot vanish. The same is true after
inverting `H`.

There is no unital algebra map

    End(k^N) -> A_H[1/H],       N>1.              (2.1)

The matrix algebra is simple, so a unital map is injective, whereas
its nontrivial orthogonal idempotents cannot inject into a domain.
Thus the exact all-matrices finite diagram cannot be mapped
multiplicatively to a scalar deformation quantization with a reduced
integral geometric special fibre.

Even on a smaller subalgebra, the literal nilpotent relation gives
a concrete symbol obstruction. The actual raising matrix obeys
`Ecal^N=0`. Any composition-preserving scalar principal-symbol map
therefore sends it to `e` with `e^N=0`, so `e=0` on the reduced
geometric chart. This is incompatible with the nonzero interior
moment-map symbol used for the geometric conjugation fields.

Matrix-valued formal targets evade the domain statement: they can
retain matrix idempotents and nilpotents. They do not thereby evade
the finite-order lemma if the adjoint action is required to become
near identity on the image. Linear maps of current complexes need
not preserve products and are not ruled out by (2.1).

## 3. Why this is a fixed-root obstruction, not a contradiction to bulk support

For fixed `N`, there is no scalar base change sending the primitive
root `Q_N` to `exp(H)` in a characteristic-zero formal field while
retaining its defining equation: it would require

    exp(NH)=1,

which is false as a formal power series for nonzero fixed `N`.
Equivalently the formal neighbourhood of `Q=1` in `Q^N=1` is the
single reduced point `H=0`.

The geometric scaling instead has `N` growing and positions of
order `1/H`, with `A=Q^a` and `Q^N=1` retained through an independent
Frobenius parameter before specialization. It is an all-level
unfolding, not the formal completion of one finite matrix algebra.
This is exactly why the proper-ratio construction in
[the partial support theorem](partial_geometric_support_theorem.md)
is legitimate: it first proves a rational contiguity identity in
independent variables and only then specializes its central parameter.
It does not map every fixed-N matrix and every finite relation into
the scalar formal coefficient algebra.

The source itself makes the distinction visible. In the finite color
algebra `C_N=k[A^+/-1]/(A^N-1)`, canonical representatives obey

    A f_tilde-(Af)_tilde=f_(N-1)(A^N-1).

The cut of `(Af)_tilde` contains `f_(N-1)`, even though ordinary
multiplication by `A` followed by the zero residue does not. This
degree-near-N carry is part of the exact source. A bounded-degree
scalar formal coefficient expansion cannot silently replace it.
The [relative source construction](relative_framing_source_transgression.md)
retains it explicitly and is linear rather than multiplicative.

## 4. What homological perturbation would prove, if its hypotheses were supplied

Here is a precise sufficient formal statement. Work in a common
H-complete **source-unfolded** category, with all endpoint and carry
components included. Suppose a complex `(C,d0)` has a contraction
onto a one-degree geometric line `G`, with maps `p,i,k` satisfying

    p i=I, d0 k+k d0=I-i p, k^2=k i=p k=0.

The line may carry its retained exponential regulator factor; scalar
coefficients and formal units are taken after that factor is fixed.
Suppose `d=d0+Delta` is a differential, and `k Delta` and `Delta k`
raise the H filtration by at least one. Define

    i_D=(I+k Delta)^(-1)i,
    p_D=p(I+Delta k)^(-1),
    k_D=k(I+Delta k)^(-1),
    d_G=p Delta(I+k Delta)^(-1)i.

All inverse operators here are the convergent geometric series in
the stipulated filtration, and `p_D=p+O(H)`. These signs use
`d0 k+k d0=I-i p`.
The identities follow by substituting
`i_D=i-k Delta i_D` and
`d0 Delta+Delta d0+Delta^2=0`; for example they give
`d i_D=i_D d_G`. The corresponding identities for `p_D,k_D` follow
by the same multiplication, yielding the perturbed contraction.
Since `G` is concentrated in one degree, `d_G=0`.

If the original marked closed source `c` is a d-cocycle and

    p(c mod H)!=0,

then `p_D c` is nonzero: its first coefficient is the displayed
nonzero projection. A compatible diagram of actual partial traces
and Ward complexes would carry this class to a scalar Ward line.
If its leading scalar map is nonzero, the perturbed scalar map is
a unit and the class survives. The exact finite cut homotopy
`Phi-p=b delta` would then identify its prescribed cut with that
scalar projection. This would be a formal source-survival theorem;
it would still assert no convergence or selected rootwise asymptotic.

The compatibility requirement is substantial. Given chain maps in
a diagram, perturbation transports them to `p_D' f i_D`, but their
nonzero leading action must be checked. Chain-map identities and
normalization of a different class do not force it.

## 5. Which hypotheses are already available

The current notes supply the following separate exact inputs:

* A nonzero transverse geometric Gaussian contraction with two actual
  framing coordinates left external, including exact contiguity.
* A literal finite relative source complex and the original
  `psi,phi,e,D`, with all canonical carries retained.
* An exact finite Hopf-adjoint partial-trace chain map for every
  matrix, and a finite cut Ward contraction onto `k I`.
* The uniform nonzero classical normal density in the marked cut
  determinant line.

They do not yet supply a common source-unfolded complex `C`, its
unperturbed source-compatible contraction, the perturbation `Delta`
realizing the actual Ward currents after transverse elimination, or
the nonzero leading scalar map on the **geometric** class. In
particular the auxiliary relative coordinate of the finite source
has not been identified with the internal Gaussian framing mode.

The finite Ward homotopy cannot merely be inserted into the formal
geometric series and declared small. Its coefficients contain

    1/(k_a-k_b)=1/[x(exp(-Ha)-exp(-Hb))]
               =1/[x H(b-a)]+O(1)

for fixed `a!=b`, and the cumulative F inverse likewise contains
`1/(1-exp(H(r+1)))`. Thus an `O(H)` correction need not make
`k Delta` topologically nilpotent. A suitable rescaled classical
complex may repair this, but its source and endpoint compatibility
must be constructed. Polynomial bounds in `N` do not establish the
required H-adic smallness.

There is therefore no justified HPL shortcut from the current
separate inputs to scalar source survival. A literal multiplicative
fixed-root-to-scalar formalization is impossible by Sections 1--2.
A linear all-level comparison, retaining the Frobenius and source
normal directions and explicitly transporting the currents, remains
possible and is the appropriate next algebraic object. The finite
all-matrices chain map alone does not construct it.
