# A uniform norm group and sourced relation complex for twist knots

Research note, 27 October 2026. This proves the one-relator side
of the determinant reduction suggested by the 4_1 and 5_2
prototypes. The twist parameter remains arbitrary throughout.
The construction comes from the actual knot-group relation,
with its return-map sign and matrix normal direction retained.
It does not assign a replacement quantum state or establish
the selected Kashaev period's volume growth.

## 1. Uniform statement

Use the signed twist presentation

    G_k=<a,b | a w^k=w^k b>, w=ab^(-1)a^(-1)b,
    k in Z, k!=0.

The hyperbolic members have k<=-1 or k>=2. Set

    A=[1 1;0 1], B=[1 0;t 1], W=AB^(-1)A^(-1)B,
    z=t^2+2, v=1+t,
    P_k(t)=S_(k-1)(z),
    f_k(t)=v S_(k-1)(z)-S_(k-2)(z),             (1.1)

where S_(-1)=0,S_0=1,S_(j+1)=z S_j-S_(j-1), extended
to all integer indices.

**Theorem.** For every k!=0:

1. The pair (f_k,P_k) is obtained by powers of one explicit
   norm-one unit in a quadratic algebra. Its norm identity is
   f_k^2+t(t-2)f_k P_k-t^3 P_k^2=1.
2. The matrix return relator has an exact quadratic normal
   form in f_k. On t!=0, its full matrix equation generates
   the scheme-theoretic ideal (f_k), retaining its first jet.
3. The polynomial f_k is monic with constant term one and
   is squarefree, even modulo 2. The classes of t and P_k
   are integral units in Z[t]/(f_k).
4. At every parabolic root, the sourced relation complex is
   acyclic. With the orbit-volume and matrix-source marks
   specified below, its torsion is exactly

       T_k^rel=-2/[P_k(t) f_k'(t)].              (1.2)

5. The weighted residue on the full integral Riley algebra
   is a perfect pairing. Its branch coefficient is
   1/[P_k(t)f_k'(t)], including all conjugate places.

This theorem is uniform in k. The comparison T_k^rel=T_beta
with the braid complex is proved by the existing exact
prototype calculations for k=-1,2; a general presentation
and quantum-source comparison is still required. No general
Gaussian-density or volume identity is inferred merely by
giving the relation torsion the same name.

## 2. A single quadratic norm group solves the twist transport

Put b=t(t-2) and introduce the quadratic algebra

    E=Q(t)[y]/(y^2-b y-t^3).

The norm of F+P y is

    N(F+P y)=F^2+b F P-t^3 P^2.                 (2.1)

Let u=1+t+y. Direct multiplication gives N(u)=1, and
multiplication by u in the basis 1,y is

    U=[1+t  t^3;1  t^2-t+1],
    det U=1, Tr U=t^2+2.                        (2.2)

Consequently

    (f_k,P_k)^t=U^k(1,0)^t                     (2.3)

for every integer k. This follows either from the Chebyshev
recurrence or from U^2-z U+I=0 and the initial values
(f_0,P_0)=(1,0), (f_1,P_1)=(1+t,1).
Taking norms proves

    f_k^2+b f_k P_k-t^3 P_k^2=1.                (2.4)

This is transport in an existing quadratic norm-one group,
with a specified unit and source point. It is not the
root-of-unity norm torsor of the quantum A-operator.
The generic splitting cover has discriminant
t^2(t^2+4). Twisting the diagram is not a manifold cover;
those operations are not being identified.

The algebra has a literal matrix realization:

    Y=W^(-1)-vI,
    Tr Y=b, det Y=-t^3,
    u -> W^(-1),
    W^(-k)=f_k I+P_k Y.                         (2.5)

Thus (2.3) is the spectral transport of the meridian
commutator itself, rather than a chosen auxiliary recurrence.

## 3. Exact matrix relator and its normal direction

The base identity A W-W B=v(A-B), followed by
Cayley--Hamilton, gives

    A W^k-W^k B=f_k(A-B).                       (3.1)

Define

    V=(A-B)B^(-1)=[-t 1;-t 0],
    Z=(A-B)B^(-1)Y=[-t^2 2t(t-1);0 t^2],
    V^#=Tr(V)I-V=[0 -1;t -t].

The inverse return relation is

    A W^k B^(-1)W^(-k)=I+P_k f_k Z+f_k^2 V.

Its inverse, with the same output-minus-input convention
as dF-I in the braid complex, is

    R_k=W^k B W^(-k)A^(-1)
       =I-P_k f_k Z+f_k^2 V^#.                 (3.2)

These are exact identities. The first follows from (3.1)
and (2.5). For the second use determinant one and
adj(I+X)=I+Tr(X)I-X in dimension two.

In particular

    Tr R_k=2-t f_k^2,
    R_k-I=-P_k f_k Z modulo f_k^2,
    Tr Z=0, det Z=-t^4.                        (3.3)

The trace alone loses the first normal direction. The
marked matrix equation retains it in the nonzero vector Z.

For completeness, the full ideal of entries of R_k-I in
Q[t,t^(-1)] is (f_k). The entries give P_k f_k and f_k^2,
since t is a unit. Equation (2.4) gives (f_k,P_k)=(1),
so these two generators generate f_k itself. The converse
inclusion is immediate from (3.2). This is a statement
about schemes, including nilpotent test rings.

## 4. All parabolic roots are simple; the source unit is integral

For k>0, f_k has degree 2k-1 and leading coefficient one.
For k=-h<0 it has degree 2h and leading coefficient one,
using S_(-j-2)=-S_j. Since S_j(2)=j+1,

    f_k(0)=k-(k-1)=1.                          (4.1)

To prove squarefreeness uniformly, work over F_2. Put
P(t)=overline(S_(k-1)(t)), Q(t)=overline(S_(k-2)(t)).
Frobenius and t^2+2=t^2 give

    overline(f_k)=(1+t)P(t)^2+Q(t)^2,
    overline(f_k')=P(t)^2.

Consecutive Chebyshev polynomials are coprime over every
field: their recurrence reduces a common divisor to the
pair S_0=1,S_(-1)=0. Thus gcd(overline(f_k),overline(f_k'))=1.
Since f_k is monic, its resultant with its derivative is
an odd nonzero integer. All characteristic-zero roots
are therefore simple, without a genericity hypothesis.

Let B_k=Z[t]/(f_k). Equation (4.1) makes t an integral
unit. Equation (2.4) gives, in this algebra,

    t^3 P_k^2=-1,
    P_k^(-1)=-t^3 P_k.                         (4.2)

Thus the source factor is an integral unit, not a factor
silently canceled only at generic complex points.

## 5. The sourced relation complex and its normalization

Let O be the noncentral trace-two conjugacy class in SL_2.
At a parabolic root, the pair (A,B) is irreducible because
t!=0. PGL_2 conjugation has an injective three-dimensional
tangent, and its quotient on O times O has coordinate
t=Tr(AB)-2. Let L be the one-dimensional matrix normal
line spanned by Z in (3.3), with the specified generator Z.

Differentiating the return relation on the fixed-trace
pair space gives the complex

    0 -> sl_2 --a--> T_(A,B)(O times O)
                               --dR_k--> L -> 0,
    a(xi)=([xi,A],[xi,B]),
    dR_k=-P_k f_k'(t) dt times Z.               (5.1)

The derivative kills conjugation because R_k=I. It is
nonzero in the remaining direction by Sections 3--4.
The complex is therefore acyclic at every root of f_k.

The source normalization is explicit. Use the ordered
sl_2 basis H=diag(1,-1), E=E_12, F=E_21. On a fixed
trace class use nu=dK wedge de/e for the matrix entries
K=G_11,e=G_12. At A use (A_11,A_12); at B use
(B_11,B_21), so nu_B=-dB_11 wedge dB_21/t.
Both forms are invariant under conjugation.

In the four tangent coordinates
(A_11,A_12,B_11,B_21), the conjugation columns and
the normal vector partial_t are

    [a(H),a(E),a(F),partial_t]
        =[0 0 -1 0;2 0 0 0;0 t 0 0;-2t 0 0 1].

Its determinant is -2t. The product orbit volume has
coefficient -1/t, so its value on these columns is 2.
The last differential in (5.1), expressed in the marked
Z basis, is -P_k f_k'. Therefore the torsion is exactly

    T_k^rel=2/(-P_k f_k')=-2/(P_k f_k').        (5.2)

Changing the complement by a conjugation column changes
neither determinant. Conjugating the pair transports all
the stated volume and source marks, so the scalar is
frame invariant. Reversing the return relation would
reverse the sign; no unmarked sign is being ignored.

## 6. A perfect residue pairing on the entire integral algebra

For a monic degree-d polynomial f define Res_f(h) to be
the coefficient of t^(d-1) in the remainder of h modulo f.
Set

    lambda_k(h)=Res_(f_k)(P_k^(-1)h).            (6.1)

The pairing (g,h)->Res_f(gh) on Z[t]/(f) is perfect:
its matrix in 1,t,...,t^(d-1) has zeros below its
anti-diagonal and ones on that diagonal. Its determinant
is (-1)^(d(d-1)/2). Multiplication by the integral unit
P_k^(-1) preserves perfection, proving the claim for
lambda_k as well. No localization at a discriminant
prime is needed for the whole algebra.

After splitting into the distinct complex root lines,
Lagrange interpolation gives

    lambda_k(h)=sum_(f_k(t_j)=0)
                         h(t_j)/(P_k(t_j)f_k'(t_j)). (6.2)

Hence the branch coefficient is exactly -T_k^rel/2.
It is a canonical weighted residue in a finite integral
algebra, with its conjugate branches retained.

## 7. What this settles and what it does not

The denominator and the -2 source normalization are now
proved uniformly on the actual twist relator side. The
commutator transport, exact normal form, all-root regularity
and integral residue pairing have proofs for arbitrary k.
They are not conclusions inferred from the prototypes.

The existing prototype computation proves T_k^rel=T_beta
and Omega_beta^2=-(T_beta/2)Omega_cut^2 for k=-1,2.
For arbitrary k, the next required map is the determinant-
and source-preserving reduction from the braid period
complex to (5.1), including its quantum lattice. The
classical group relation alone does not supply that map.

Even after that map, the actual global quantum source
must have its regulator norm controlled across levels.
This note does not prove the original volume conjecture,
or replace Kashaev by the classical residue (6.1).

The general program now uses the
[arbitrary-bridge sourced complex](arbitrary_bridge_source_reduction.md),
with unrestricted bridge number and crossing word. The calculation
above is retained as a one-relator diagnostic. A separate executable
uniform-twist audit is not attached to this proof text.
