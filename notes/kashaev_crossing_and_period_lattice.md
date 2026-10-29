# The specified Kashaev crossing and its period pairing

Research note, 25 October 2026. This uses Kashaev's crossing weights,
[q-alg/9504020](https://arxiv.org/abs/q-alg/9504020), equations (2.7)--(2.12),
and the enhanced braid definition recorded in Murakami--Murakami,
[math/9905075](https://arxiv.org/abs/math/9905075), Sections 1 and 4.
Their comparison proofs are not premises. We derive the Fourier identity
and normalization comparison below directly from finite products.

This is an independent verification of a known comparison, not a new
volume theorem. It fixes the literature state to which a quantum
A-module argument must apply. All integers N>=2, including even and
composite levels, are allowed.

The subsequent [Casimir/lattice comparison](casimir_braiding_and_recoupling_lattice.md)
expresses this same crossing and its inverse by confluent Casimir
polynomials, retaining the double-point derivatives and exact writhe
phase. It also derives the actual pivotal closing trace on that
spectral algebra and identifies the operators through the singular
cyclic recoupling lattice.

## 1. The Fourier transform is triangular

Put omega=exp(2*pi*i/N), p_j=product_(h=1)^j(1-omega^h), p_0=1,
and bar_p_j=product_(h=1)^j(1-omega^(-h)). Let R^o be exactly the
unbraided matrix in Kashaev's equation (2.12). Use

    F_ij=omega^(ij)/sqrt(N),       A=(F^(-1) tensor F^(-1))
                                    R^o(F tensor F).

**Fourier identity.** With indices in {0,...,N-1}, the only nonzero
entries are

    A_(a-k,b+k ; a,b)
       =omega^(1+(a-k)(b+1))
          p_a p_(b+k)/(p_(a-k) p_b p_k),
    0<=k<=min(a,N-1-b).                               (1.1)

In particular, conservation here is equality of ordinary integer sums,
not just equality modulo N.

### Direct proof

For a nonzero original entry introduce residues

    u=[j-i-1], v=[i-l], t=[l-k], h=[k-j].

The two theta factors say u+t<N and v+h<N. Their total is congruent
to -1 modulo N, so u+v+t+h=N-1. Conversely every such composition and
one free j specify exactly one original entry. In these coordinates,

    i=j-1-u, k=j+h, l=j+h+t  (mod N),
    R^o_(i,j ; k,l)=N omega^(1-(t+h)(u+h))
                           /(p_u bar_p_v p_t bar_p_h). (1.2)

The free j-sum in the Fourier transform gives the conservation delta.
Put z=t+h. The remaining sum factors into

    A_(c,d ; a,b)=delta_(a+b=c+d mod N)
      sum_(z=0)^(N-1) omega^(1+c-z^2+z(a+b))
        S_(N-1-z)(omega^(c-z)) S_z(omega^(z-a)),       (1.3)

where the elementary finite binomial identity is

    S_m(X)=sum_(j=0)^m X^j/(p_j bar_p_(m-j))
          =product_(j=1)^m(X-omega^j)/p_m.            (1.4)

For a direct induction, use bar_p_m=(-1)^m omega^(-m(m+1)/2)p_m
and compare coefficients in
(1-omega^m)S_m(X)=(X-omega^m)S_(m-1)(X).

The first factor in (1.3) vanishes unless c<=z; the second vanishes
unless z<=a. Using p_(N-1)=N and the same formula for bar_p_j,
the surviving sum, with m=a-c, is

    omega^(1+c(b+1)) (p_a/p_c)
      sum_(j=0)^m (-1)^j omega^(j(j-1)/2)
                          omega^((b+1)j)/(p_j p_(m-j))
    =omega^(1+c(b+1)) (p_a/p_c)
                           (omega^(b+1);omega)_m/p_m. (1.5)

The last equality follows from the same finite binomial identity.
If b+m>=N, this Pochhammer symbol contains 1-omega^N and vanishes.
Otherwise d=b+m as an ordinary integer and the symbol is p_(b+m)/p_b.
This proves (1.1), with no primality assumption.

## 2. A literal comparison with the root-of-unity quantum-group matrix

Let s=exp(pi*i/N), H_j=N-1-2j, and use the N-dimensional highest-weight
module with

    H v_j=H_j v_j, K v_j=s^(H_j)v_j,
    E v_j=[j]_s^2 v_(j-1), F_low v_j=v_(j+1).

At the endpoints the missing vectors are zero. These are the specialized
usual matrices E v_j=[j]_s[N-j]_s v_(j-1), since [N-j]_s=[j]_s.
Let

    R^q=s^(H tensor H/2)
       sum_(k=0)^(N-1) s^(k(k-1)/2)(s-s^(-1))^k/[k]_s!
                                      E^k tensor F_low^k. (2.1)

Every denominator in (2.1) is nonzero. Put

    G_j=p_j/(1-omega)^j=s^(j(j-1)/2)[j]_s!,
    D_j=(-s)^j,
    gamma=omega*s^(-(N-1)^2/2).

Then (1.1) gives exactly

    A=gamma (D G tensor G) R^q
                         (G^(-1) tensor G^(-1)D^(-1)). (2.2)

Here G,D are diagonal. To verify (2.2), substitute the matrix elements
of E^k and F_low^k in (2.1), replace each [j]_s! by
s^(-j(j-1)/2)p_j/(1-omega)^j, and cancel. The remaining exponent and
factorials are precisely those in (1.1). Thus exponentially large
factorials in G have not been declared harmless; their positions in
the exact conjugations remain specified.

## 3. The published enhancement and every braid word

Let P swap tensor factors, and let S v_j=v_(j+1 mod N). In the
enhanced Kashaev convention used here,

    B_K=P(R^o)^T,       mu_K=-s S,       alpha_K=-s,
    beta_K=1.                                         (3.1)

The transpose/order in (3.1) matters. Substituting (2.8) of Kashaev
in P(R^o)^T gives exactly the four-index enhanced crossing definition.
For the quantum-group dual convention put

    B_q=P(R^q)^T,       mu_q=K^(-1),
    alpha_q=s^((N^2-1)/2),       beta_q=1.             (3.2)

Equation (2.2), transposed and with the tensor factors exchanged, gives
a similarity of B_K with gamma*B_q. For a braid on b strands, define

    U_b=F^(-tensor b) tensor_(j=1)^b (G^(-1)D^(j-1)).

The meaning is the product of F^(-tensor b) with the displayed diagonal
tensor product. Since B_q conserves the integer weight sum, it commutes
with D tensor D. Thus the same U_b works simultaneously for every
adjacent generator and its inverse:

    rho_K(word)=gamma^(w(word)) U_b rho_q(word) U_b^(-1).
                                                               (3.3)

The enhancement also matches exactly:

    U_b mu_q^(tensor b) U_b^(-1)=mu_K^(tensor b),
    gamma*alpha_q=-s=alpha_K.                         (3.4)

For the first identity, diagonal G,D commute with mu_q and
F^(-1)diag(omega^j)F=S; also s^(-(N-1))=-s.

The quantum-group partial traces have values alpha_q and alpha_q^(-1).
One way to verify the scalars is to use the coproduct intertwining
equations for (2.1) and trace cyclicity: the weighted partial traces
commute with the dual module's generators. These act irreducibly because their
adjacent coefficients are nonzero and the K eigenvalues are distinct.
The traces are therefore scalar. The positive trace at v_(N-1) and
negative trace at v_0 each have a single contributing term, giving
s^((N^2-1)/2) and its inverse. The coproduct equations themselves reduce
to the coefficient recurrence

    c_(k+1)/c_k=s^k(s-s^(-1))/[k+1]_s

of the finite sum (2.1). These checks are elementary algebra and do
not invoke a global state-integral theorem.

For a braid closure with one component, cut the first strand and take
the weighted partial trace over the others. The unnormalized operator
is scalar: it is a quantum-group endomorphism of the simple color.
Conjugations on the traced factors cancel by cyclicity; conjugation
on the open factor cancels because this operator is scalar. Finally
the factors gamma^(w) cancel against alpha_K^(-w) by (3.4).

**Consequence.** The normalized enhanced Kashaev period in (3.1) equals
the reduced N-colored quantum-group period at s=exp(pi*i/N), with
unknot value one. This holds for every braid presentation of a knot
and every N>=2. It is a direct independent verification of the standard
enhanced-state comparison, not an appeal to its published proof.
The usual quantum-group parameter for the colored Jones polynomial
is omega=s^2; the chosen dual and tensor-order convention is retained.

## 4. A printed phase needs attention

The literal candidate inverse printed in Kashaev's (2.15), combined with
the normalization (2.12), fails the identity (2.16) already at N=2:
the product is -I. This is checked in characteristic zero with rational
entries. The exact cyclotomic diagnostics at further levels give
omega*I. We use the actual matrix inverse in (3.3), determined by
(2.2), rather than silently deleting this phase.

This observation concerns a printed normalization identity, not a
counterexample to the knot volume conjecture. The enhanced definition
(3.1) specifies its own actual inverse and scalar normalization.

## 5. Reproducible algebraic checks and scope

`experiments/audit_kashaev_crossing.py` evaluates the original four-index
weight independently of (1.1), checks its complete Fourier transform,
the quantum-group matrix comparison, and the enhanced partial traces.
It includes even and composite levels. Prime-field diagnostics are
supplementary to the characteristic-zero identities proved above.

The coefficient and enhancement identities fix a literature state
uniformly, with no FAMED hypothesis or knot census. They do not prove
the AJ conjecture or the Kashaev volume conjecture. In particular, they
do not make the AK/Faddeev contour state equal to this finite period.
That is a different comparison.

A standard noncommutative A-polynomial can now be discussed together
with this distinguished reduced quantum-group period, rather than
an arbitrary solution of its recurrence. Root-of-unity periodicity
and the geometric q->1 branch must still be distinguished in its
period-torsor comparison.
