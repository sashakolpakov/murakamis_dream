# Auditing the ordinary-color remainder in the original Fourier energy

28 October 2026. The question is the precise inequality used when replacing
the original complete-color value by a positive Fourier norm. The proof
below uses the actual finite crossing matrices and a reconstructed positive
path trace. No published asymptotic, unitarity, ADO/Jones comparison, or
volume-conjecture theorem is a premise.

The root convention is essential. Set

    q=exp(pi i/N), Q=q^2,
    [j]=sin(pi j/N)/sin(pi/N).

Let a fixed braid on b strands close to a ONE-component zero-framed knot,
and let C_j(q) denote its original reduced ordinary j-color, with unknot
value one. Then, for every 1<=j<N,

    |C_j(q)| <= [j]^(b-1) <= sin(pi/N)^(1-b).       (1)

There is no corresponding assertion at j=N. The statement is also not
asserted at arbitrary Galois-conjugate roots.

The immediate consequence needed in the Fourier argument is the
all-level, all-ordinary-color estimate

    0 <= E_N-|K_N|^2 <= (N-1)(N/2)^(2b-2).       (1a)

Here the braid presentation, and therefore b, is fixed as N varies.
Neither hyperbolicity nor alternatingness is needed for this bound.
The positive-energy identity is exact; only the replacement of its
ordinary-color remainder by a polynomial uses the estimate.

## 1. The positive algebra and its trace can be checked directly

Put delta=q+q^(-1)=2cos(pi/N), and
mu_a=sin((a+1)pi/N)/sin(pi/N), 0<=a<=N-2. These numbers are positive;
with zero boundary values they satisfy mu_(a-1)+mu_(a+1)=delta mu_a.
On walks of length m in the chain 0,...,N-2 starting at zero, let U_i
change only the middle height of a return (c,a,c), with coefficient
sqrt(mu_a mu_a')/mu_c. Direct local multiplication gives

    U_i*=U_i, U_i^2=delta U_i,
    U_i U_(i+1) U_i=U_i,
    U_i U_j=U_j U_i for |i-j|>1.

Consequently B_i=q^(1/2)I-q^(-1/2)U_i is unitary: its eigenvalues are
q^(1/2) and -q^(-3/2). The same displayed relations prove the braid
relation. Inverse crossings are the actual inverses.

The weighted trace

    tau_m(A)=sum_walks mu_(last height) A_(walk,walk)

is positive. Its weight is central in the path algebra because every
generator preserves the last height, so it is tracial too. Directly,

    tau_(m+1)(A tensor I)=delta tau_m(A),
    tau_(m+1)((A tensor I)U_m)=tau_m(A).            (2)

In the first identity sum over the last step using the mu recurrence.
In the second identity only the unchanged middle height contributes to
the diagonal: mu_c from the last vertex cancels the denominator mu_c of
U_m, leaving exactly the weight mu_a on the length-m walk.

These recursions identify the trace with the original fundamental
quantum trace. Indeed the latter has K=diag(q,q^(-1)) and U block
[[q,-1],[-1,q^(-1)]] on (01,10), zero on (00,11); its partial K-trace
is I and Tr K=delta. Both traces therefore satisfy (2), with value one
on the empty diagram. Uniqueness does not require semisimplicity:
the Temperley--Lieb relations inductively span the next algebra by
the included algebra and elements A U_m B, and traciality plus (2)
determine both types. The spanning claim follows by reducing each
U_m A U_m with the preceding spanning statement and the two local
quadratic/adjacent relations.

## 2. Ordinary colors are positive projections in this trace

Write n=j-1. The recursively defined color projector is

    p_0=p_1=I,
    p_(m+1)=p_m tensor I
       -[m]/[m+1] (p_m tensor I)U_m(p_m tensor I).

For n<=N-2 every denominator used is nonzero and every coefficient
is real. The local algebra proves idempotence and annihilation by
U_1,...,U_(n-1); hence its path realization is an orthogonal projector.
The trace recursion gives tau_n(p_n)=[n+1]=[j].

This is the actual highest-weight color, not a color assigned to an
unrelated positive model. In the ordinary fundamental tensor space,
the common kernel of the U_i has one vector at each tensor weight:
the local 01/10 relation fixes their coefficient ratio and adjacent
exchanges connect all words of that weight. The vectors obtained by
successive coproduct F-actions on the highest tensor span those lines.
Their coefficients involve only nonzero [r]!, r<=n. Thus they give
the original j-dimensional highest-weight module. The projector acts
as identity on this common kernel and has image in it. Restricting
the cabled finite universal R to these images gives the original
j-color R, by its coproduct identities. A direct coefficient proof of
both identities, including the Cartan factors, is given in the
[independent color audit](actual_ordinary_color_comparison_audit.md#4-the-fundamental-cable-is-the-literal-colored-r).
The retained highest-vector
Cartan scalar is q^(n^2/2); the ordinary framing twist is
q^(n(n+2)/2). Both have modulus one.

For b colored strands let P be the tensor product of these projectors.
The trace of a disjoint colored closure, or (2) successively, gives

    tau(P)=[j]^b.

The cabled braid is unitary in the path representation and preserves
P. It also preserves each last-height block. In an orthonormal basis
of Im P within each such block, its diagonal entries have modulus at
most one and every trace weight is positive. Therefore

    |tau(P B P)| <= tau(P)=[j]^b.

Dividing by the NONZERO original ordinary quantum dimension [j],
and retaining the unit-modulus zero-framing factor, proves (1).

At j=N the relevant quantum dimension is [N]=0. In the positive path
trace the corresponding negligible projector has zero image. The
division just used is unavailable. This is precisely why this proof
places no polynomial bound on K_N.

## 3. The ADO orbit really has these ordinary-color values

At the orbit color x=q^(j-1), the original N-dimensional module has
the invariant subspace U=span(v_j,...,v_(N-1)); its quotient is the
ordinary j-dimensional module. Every tensor factor of the finite R,
its inverse, and the pivot preserves U. In a basis adapted to U,
each matrix path along an underlying strand can enter U but cannot
leave it. A one-component braid closure passes through the open cut.
For its quotient block that cut starts and ends outside U, forcing
every contributing path around the component to stay in the quotient.
Thus the induced cut is exactly the all-j-colored cut, even though
the other braid strands were traced first. No assertion of this form
is made for a separate closed link component.

The conventions agree after the explicit signs are kept:

    K^(1-N)=epsilon_j K,
    theta_ADO=epsilon_j theta_ordinary,
    epsilon_j=(-1)^(j-1).

The braid permutation is a b-cycle, so its writhe w satisfies
w=b-1 modulo 2. The resulting sign is
epsilon_j^(b-1-w)=1. Consequently the original even meridian family
satisfies F_N(Q^j)=C_j(q), with F_N(1)=K_N. This is the filtered
matrix argument of `root_orbit_pointing.md`, with the precise
one-component and framing hypotheses exposed.

To distinguish the two coordinates used in the older notes, write this as

    F_N^M(-q^j)=F_N^Y(Q^j)=C_j(q), Y=M^2.

The functions in this identity are REDUCED periods. The full ADO state
also carries its original modified-dimension factor, which can have a
pole at an ordinary orbit point. Neither its value nor a transverse
derivative is bounded by (1). No such value or derivative is used in
the Fourier remainder below.

## 4. An explicit positive Fourier remainder

Set c_0=K_N and c_j=C_j(q) for 1<=j<N, and use the unitary transform

    chat_k=N^(-1/2) sum_(j=0)^(N-1) Q^(-kj)c_j.

Finite character orthogonality proves exactly

    E_N:=sum_k |chat_k|^2
       =|K_N|^2+R_N,
    0<=R_N=sum_(j=1)^(N-1)|C_j(q)|^2
       <=sum_(j=1)^(N-1)[j]^(2b-2).               (3)

In particular this remainder is polynomial uniformly over the entire
ordinary-color range, including j=N-1, rather than just at fixed j.
There is an explicit sharper constant. Put r=b-1>=1 and assume N>r.
The Fourier expansion of sin^(2r)(pi j/N) has frequencies -r,...,r.
Only its constant coefficient survives summation over all N roots;
that coefficient is binom(2r,r)/4^r. The j=0 summand is zero. Hence

    0<=R_N <= N binom(2r,r)/(4^r sin^(2r)(pi/N))
            <= binom(2r,r) N^(2r+1)/16^r.         (4)

For b=1 the closure is the unknot and R_N=N-1 instead. For small
N<=r the sum bound (3) remains valid without the simplified formula.

Equivalently chat=K_N u+e, where u is the constant unit vector,
e is orthogonal to u, and ||e||^2=R_N. This orthogonality is exact;
there is no discarded cross term.

There is also an unconditional logarithmic statement, which is safer
than writing an equality of unsmoothed logarithms before a positive
rate has been established. The trivial ordinary color satisfies C_1=1,
so R_N>=1 for every N>=2. Set

    P_(N,b)=(N-1)(N/2)^(2b-2)>=1.

Then the exact energy identity and (1a) give

    1+|K_N|^2 <= E_N <= P_(N,b)(1+|K_N|^2),       (4a)
    0 <= log E_N-log(1+|K_N|^2) <= log P_(N,b).

In particular, uniformly without any nonvanishing assumption,

    (pi/N)log E_N
      =(pi/N)log(1+|K_N|^2)+O_b(log N/N).         (4b)

With log 0=-infinity this is equivalently

    0 <= (pi/N)log E_N-max(0,(2pi/N)log|K_N|)
       <= (pi/N)log(2P_(N,b)).                   (4c)

For any fixed V>0, (4a)--(4c) prove

    (2pi/N)log|K_N| -> V
        if and only if
    (pi/N)log E_N -> V.                           (5)

The implication from positive energy to the original invariant uses
the fact that a polynomial remainder is smaller than any sequence
with strictly positive exponential rate. It does not assume eventual
nonvanishing of K_N; that nonvanishing follows from the positive energy
rate and (3). An unrestricted equality of log E_N and 2 log|K_N| at
exponential scale does NOT follow merely from the polynomial remainder:
zeros or exponentially small values would invalidate that inference.

## 5. What is verified, and what remains

The finite Plancherel checks do not establish a volume limit. The remaining analytical questions are stated below.

* [Positive path algebra](ordinary_color_positive_trace_independent_audit.md):
  both Markov identities on noncommuting words, the full projection
  induction including the first zero-dimension projection, and 42 signed
  colored closures including j=N-1.
* [Original color identification](actual_ordinary_color_comparison_audit.md):
  the uniform one-component filtered trace proof and direct R coproduct
  calculation, supplemented by 228 exact whole-knot cut comparisons and
  22 signed-cable families, with the original Cartan and twist phases.

The explicit sine-energy identity in (4) was independently checked in
225 pairs (N,r), with 80-digit arithmetic; its proof is the finite
character calculation above. No defect was found in either uniform
proof. These checks establish the remainder estimate's stated scope,
not the geometric size of the remaining Fourier energy.

The polynomial remainder in (3) has an independent algebraic proof.
The positive energy E_N still requires its geometric exponential
estimate. In particular, the canonical cleared operator B(Y-1)
becomes Bhat(S-I) in the dual cyclic coordinate and kills the constant
mode u exactly. Retaining the original normal/pointed source is
therefore essential when estimating that energy. Plancherel validates
the positive target; it does not by itself supply its size.
