# The actual multi-leg source has no nonzero two-sided null ideal

Research proof, 27 October 2026. For three or more strands, the original
pivotal highest-input source on the FULL Borel-relative word algebra
does not factor through any proper algebra quotient. Every path
coefficient can be detected after actual relative matrix coupons.
For two strands its maximal null ideal is instead explicit, and the
minimal algebra quotient is the triangular path algebra of a line.

This is a boundary on algebraic reductions of the entire relative
algebra, not an obstruction to a linear relative-period transform,
a current-complex quotient, a singular geometric comparison, or a
quotient of a smaller actual-word/observable algebra. In particular
it does not disprove the volume conjecture. It specifies what a
source-preserving attempt to discard the nilpotent shell would need
to avoid.

## 1. The actual algebra and the relevant notion of source quotient

Fix an original root Q of order N>=2. Let

    A_0=<H,f | H^N=1, Hf=Q^-1 fH, f^N=0>,
    z_(a,j)=f^a e_j, 0<=a,j<N.

The exact multiplication is the one in
[the actual Borel fusion theorem](actual_borel_regular_fusion_and_divided_cap_period.md).
Think of z_(a,j) as an oriented path of length a starting at j
and ending at j+a modulo N. A product whose total length is at
least N is zero.

On b strands that theorem identifies the actual tensor module
with a free LEFT A_0 module of rank r=N^(b-2). Consequently the
full Borel-relative endomorphism algebra is

    B_b=Mat_r(A_0^op).

The original source is the actual pivotal partial trace on all
but the first strand, followed by first input e_0 and output
ell=ones^t. In coefficient form write

    Psi(T)=sum_(t,s) Lambda_(t,s)(a_(t,s)).            (1)

Here T_(t,s)=R_(a_(t,s)) acts by right multiplication in the
regular algebra. All original external factors may be included
or retained externally. At a regular complete fiber they are
nonzero, so they do not change any null ideal below.

Define the maximal two-sided source-null ideal by

    I_Psi={T : Psi(U T V)=0 for every U,V in B_b}.    (2)

It is the largest two-sided ideal contained in ker(Psi). If an
algebra homomorphism pi:B_b->C preserves the source, meaning
Psi=lambda composed with pi, then ker(pi) is contained in (2).
This formulation does not assume that an arbitrary geometric
relative-period map is an algebra homomorphism.

## 2. Literal physical top rows detect all residue classes

Use the original full fusion basis, not the later tail-head
decomposition. Its tail labels are

    s=(s_3,...,s_b), 0<=s_i<N.

The seed associated with f^a e_k in copy s is

    f_total^a(e_0 tensor e_(k-sum(s) mod N) tensor e_s).

Let X=product_i x_i be the product of the actual highest K roots.
The source of the diagonal relative top path is exactly

    Lambda_(s,s)(f^(N-1)e_k)
       =gamma_s delta_(k,sum(s) mod N),
    gamma_s=N X^(1-N) Q^(1-sum(s)), gamma_s!=0.       (3)

This is a direct physical cap calculation. Returning every tail
output to its input s forces zero lowering steps on those legs.
For the remaining N-1 steps to return the second output to the
required pivotal index, all of them must go to the second leg,
whose initial index must be zero. Thus k=sum(s) modulo N; any
other k would require N first-leg lowering steps, impossible
in total degree N-1. The coefficient of the second-leg steps is
F_(N-1)=N, and their K_1 inverses supply x_1^(1-N).
The second pivotal entry contributes x_2^(1-N)Q, while the tail
pivots contribute product_(i>=3) x_i^(1-N)Q^-sum(s). This is (3).

The all-ones first output row remains the actual one; only its
zero-index entry occurs in this particular top-row calculation.
No normalized trace or geometric co-source is substituted.

## 3. For b>=3, no relative algebra ideal can be discarded

**Theorem.** For b>=3, I_Psi=0.

Take a nonzero element T of a two-sided ideal I in B_b.
Some coefficient a_(t,s) has a nonzero coefficient c of
f^a e_j. Relative matrix units first move that entry to any
chosen diagonal copy; left/right coefficient idempotents isolate
it, because

    e_(j+a) a_(t,s) e_j=c f^a e_j.                  (4)

Only one degree between zero and N-1 has that start and endpoint.
Multiplication by f^(N-1-a) then gives

    f^(N-1-a) [c f^a e_j]=c f^(N-1)e_j.            (5)

All these operations are allowed relative matrix coupons, so the
result stays in I. For b>=3 choose a diagonal tail copy u with
sum(u)=j modulo N, for instance u_3=j and all later u_i=0.
Equation (3) evaluates the resulting element to c gamma_u!=0.
Thus no nonzero ideal is contained in ker(Psi), proving the theorem.

The coefficient algebra is opposite to physical operator composition;
this only exchanges which of the two matrix-coupon sides realizes
the left or right coefficient factor in (4)-(5). Both sides are
available in (2), so no commutativity assumption enters the proof.

In particular ANY source-preserving algebra quotient of B_b is
injective. This includes nilpotent ideals: the entire radical
cannot be removed, nor can a nonzero subideal of it. The result
is stronger than an example of one nonzero radical contribution.

It does not say Psi(UT) alone is a nondegenerate bilinear pairing;
the proof uses both coupon sides. Nor does it say that every
relative coupon is an actual braid word or commutes with the full
quantum-group E action. The algebra in the theorem is the full
actual Borel commutant furnished by fusion. A reduction on a
strictly smaller operator algebra needs its own analysis.

## 4. The two-leg contrast: the exact quotient is triangular

For b=2, the actual cap is

    Lambda(f^a e_k)=x_2^(1-N) x_1^-a Q^-(k+a)
                         F_(k+a)/F_k,  if k+a<N,
                   0,                 if k+a>=N.    (6)

Define the wrapped-path span

    I_cut=span{f^a e_k : k+a>=N}.                    (7)

It is a two-sided ideal: further path concatenation cannot undo
crossing the cut from N-1 to zero, and paths of total length at
least N vanish. The source (6) kills it. Conversely every
nonwrapped path has a nonzero source value, and the two endpoint
idempotents isolate its coefficient as in (4). Thus no larger
two-sided ideal lies in the source kernel, so

    I_Lambda=I_cut,
    dim I_cut=N(N-1)/2.                             (8)

The quotient is the lower triangular N-by-N matrix algebra under

    f^a e_k -> E_(k+a,k) if k+a<N, and zero otherwise.

This respects the path multiplication and gives all triangular
matrix units. Its dimension is N(N+1)/2. In these coordinates
the original cap is the matrix coefficient

    Lambda(T)=x_2^(1-N) r^t T c,
    r_i=x_1^-i Q^-i F_i, c_k=x_1^k/F_k.             (9)

Every r_i and c_k is nonzero. The effective triangular nilpotence
length still grows with N. Its existence does not provide a
bounded-rank critical algebra or a subexponential coefficient bound.

The b>=3 theorem explains why one cannot apply this two-leg
quotient independently to intermediate diagonal blocks of a
multi-strand word. Off-diagonal tail transitions expose all
cyclic residue classes before the final selected contraction.
Only the completed word may be passed to the diagonal-source
formula of [the all-strand Euler/Cauchy theorem](all_strand_euler_cauchy_cap.md).

## 5. Consequence for the geometric comparison

The exact endpoint functional is a tractable finite linear source,
but its full algebra source does not descend to a smaller algebra
by deleting a null ideal once b>=3. A fixed geometric critical
algebra cannot be obtained as such a quotient of B_b while retaining
all sourced relative matrix coupons. Morita equivalence may remove
the matrix factor, but A_0 still has N simple modules and Loewy
length N, so it is not Morita equivalent to one fixed finite etale
critical algebra as N grows.

This specifies the kind of comparison still available: a linear
relative-period or current-complex map, a separately constructed
singular/nonlocal transform, or a restriction to an actual smaller
meridian/word algebra with a proved invariant source quotient.
Zero-source linear current spaces need not be ideals, so they are
not excluded by the theorem. The result does not establish a
nonzero selected geometric class or a volume norm.

## 6. Exact checks

[The audit](../experiments/audit_actual_source_two_sided_quotient.py)
and its [saved results](../experiments/actual_source_two_sided_quotient_results.json)
check (3) against the literal original physical source after the
actual coproduct fusion for braid indices three and four. They
also check all relative matrix-basis coefficient recovery
certificates in (4)-(5), and the two-leg wrapped ideal at levels
two through eight. The proof above is all-level and does not
depend on a finite rank fit or on an assertion about untested knots.

The full Borel commutant and the algebra generated by the actual quantum words are different objects. The conclusion uses the latter as specified.