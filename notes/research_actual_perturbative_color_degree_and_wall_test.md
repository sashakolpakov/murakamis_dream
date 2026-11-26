# A direct perturbative degree bound for the actual knot source

Private research proof, 17 November 2026.

This note makes a degree estimate explicit in the original cut-braid
proof of color polynomiality. It proves the weak bound
\[
 C_j(e^h)=\sum_{n\geq0}p_n(j)h^n,\qquad
 p_n\in\mathbb C[j],\qquad \deg p_n\leq2n.             \tag{1}
\]
Here \(C_j\) is the actual reduced, zero-framed ordinary color of a
fixed oriented knot, with unknot value one. The proof uses its ordinary
pivot, cut, and framing normalization. It is not a claim of novelty
for perturbative color theory, and does not use the stronger
Melvin--Morton degree bound.

The only proof sources are [A](adequacy_and_algebraic_periods.md),
especially its Section 5, and
[B](bounded_normal_color_transfer.md), Section 3.
A supplies the actual cut-braid source and its polynomiality argument.
B supplies the particular source-wall modification tested below.
All degree estimates needed here are proved explicitly.

## 1. Degree bookkeeping in the formal quantum group

Put \(q=e^h\), and use the ordinary generators with
\[
 [H,E]=2E,\qquad [H,F]=-2F,\qquad
 [E,F]=\frac{\sinh(hH)}{\sinh h}.                    \tag{2}
\]
Give each of \(E,F,H\) word degree one, and add these degrees over
tensor factors. Coefficients and degrees below are formal in \(h\);
no uniform analytic expansion in the color is asserted.

For every \(a\geq0\), the coefficient of \(h^a\) in the last expression
of (2) is a polynomial \(Q_a(H)\) with
\[
 Q_a=0\ \text{for odd }a,\qquad \deg Q_a\leq a+1.
                                                               \tag{3}
\]
Indeed, write that expression as
\[
 \left(\sum_{r\geq0}\frac{h^{2r}H^{2r+1}}{(2r+1)!}\right)
 \frac{h}{\sinh h}.
 \]
The last factor is a scalar power series with constant term one.

Consequently, straightening a word of length \(L\) into
\(F^\alpha H^\beta E^\gamma\) contributes, at additional order
\(h^a\), only PBW monomials of degree at most \(L+a\).
To see this directly, moving \(H\) past \(E\) or \(F\) replaces
\(H\) by \(H\pm2\) and does not increase degree. In an \(EF\)
interchange, the \(FE\) term preserves length, while using
\(h^aQ_a(H)\) replaces two letters by at most \(a+1\) letters.
It therefore increases length by at most \(a-1\), and in particular
by at most \(a\). Along a straightening term these added orders sum.
Every use of a commutator term removes two \(E,F\) letters; the other
interchanges reduce their inversions. Thus the process is finite at
each fixed order and proves the stated bound.

In particular, if before straightening an order-\(h^k\) term has
length at most \(2k\), then its contribution at total order \(n=k+a\)
has PBW degree at most
\[
 2k+a\leq2n.                                      \tag{4}
\]

## 2. The original crossings and cut obey this degree budget

The unpermuted ordinary crossing in A is the product of a Cartan
factor and the nilpotent series. Its relevant factors have the form
\[
 \exp(hH\otimes H/2),\qquad
 \sum_{r\geq0}u_r(h)
       \frac{(e^h-e^{-h})^r}{[r]_{e^h}!}\,
       E^r\otimes F^r,                            \tag{5}
\]
where \(u_r(h)\) is a scalar formal unit. Interchanging the two
tensor conventions does not change any degree below. Since
\([r]_{e^h}!\) has nonzero constant term \(r!\), the \(r\)-th
nilpotent term starts at order \(h^r\) and has word degree \(2r\).
The order-\(h^a\) Cartan term has degree \(2a\). Therefore the
order-\(h^n\) crossing has total tensor word degree at most \(2n\).
Only finitely many nilpotent indices \(r\leq n\) occur at that order.

This property is closed under products, simply by concatenating
words. It is also closed under the formal inverse of a series with
constant term the identity: expand the inverse in powers of its
positive-order part. Thus the actual inverse crossing satisfies the
same estimate. The ordinary pivotal factors
\(\exp(\pm hH)\) have degree at most their order, so satisfy it too.
No singular factorial change to a self-dual basis is used.

Choose a fixed braid whose closure is the knot, and cut one of its
closure arcs. Write every checked crossing as its flip times an
unpermuted crossing. Move the flips through the tensor words to one
end. This permutes tensor slots and preserves total word degree.
At any fixed \(h\)-order the result is a finite sum of a permutation
times tensor words, with the ordinary pivotal factors retained.

The permutation of this braid has exactly one cycle, because its
closure has exactly one component. Its cut contraction is therefore
one ordered product of all the tensor words and pivotal insertions
along that cycle. In ordinary dual bases, cups and caps identify
matrix indices by Kronecker symbols, with the displayed pivot at a
pivotal cap. Following those identifications around the single cycle
leaves the cut input and output and no independent closed index
cycle. Thus no separate trace or color-dimensional factor remains.
This is the literal matrix contraction used in A, not a replacement
of the original closing by a positive or factorial-gauged functional.

At order \(h^n\), the resulting cut operator is consequently a finite
sum of words with the budget used in (4). Straighten them. In the
ordinary \(j\)-dimensional highest-weight module,
\[
 Ev_0=0,\qquad Hv_0=(j-1)v_0,
 \]
and \(F\) lowers weight. The \(v_0\)-to-\(v_0\) entry of
\(F^\alpha H^\beta E^\gamma\) is zero unless
\(\alpha=\gamma=0\), in which case it is \((j-1)^\beta\).
Equation (4) proves that the order-\(h^n\) highest entry has degree
at most \(2n\) in \(j\).

This is one polynomial valid for every positive integer \(j\), not
merely for \(j>n\). The same universal word identity acts on every
finite highest-weight quotient. Nilpotent crossing terms beyond its
dimension vanish in that quotient; no separate truncation correction
is added to the universal highest entry.

The ordinary cut intertwiner is scalar at generic \(q\), so this
highest entry is the framed reduced scalar of the original source.
There is no subsequent division by the color dimension. To obtain
the stated zero-framed \(C_j\), remove the actual scalar curl to the
power prescribed by the braid writhe. The same argument applies to
that fixed one-curl cut diagram: its scalar has constant term one
and its order-\(h^n\) coefficient has degree at most \(2n\).
Products and formal inverses of scalar series with this property
preserve it. Hence the actual framing correction preserves the bound.
This also agrees with the usual exponential of \(h\) times the
quadratic highest-weight twist, but no alternate off-root pivot or
framing is substituted. We obtain (1), with \(p_0=1\).

The one-component hypothesis was used at the cut contraction. For a
link with further closed components, independent traces remain, so
the above proof does not assert (1) for that differently normalized
source.

## 3. Test of the original multiplicative wall modification

Fix positive integers \(J,m\). Retain precisely the construction
of B:
\[
 a_r(q)=q^{2r}+q^{-2r},\qquad
 R_J(q,Y)=
 \prod_{r=1}^J\frac{Y+Y^{-1}-a_r(q)}{2-a_r(q)},
 \qquad h_{J,m}=(1-R_J)^m,                         \tag{6}
\]
\[
 \widetilde C_j(q)
 =1+h_{J,m}(q,q^{2j})\bigl(C_j(q)-1\bigr).         \tag{7}
\]
B proves that these fixed-color expressions are Laurent polynomials
and have value one at \(q=1\). Their limiting multiplier has a simple
exact form. For each fixed \(j\),
\[
 a_j(e^h)-a_r(e^h)=4(j^2-r^2)h^2+O(h^4),\qquad
 2-a_r(e^h)=-4r^2h^2+O(h^4).
 \]
Therefore
\[
 R_J(e^h,e^{2jh})
 =\prod_{r=1}^J\left(1-\frac{j^2}{r^2}\right)+O(h^2),
 \qquad
 h_{J,m}(e^h,e^{2jh})=H_{J,m}(j)+O(h^2),           \tag{8}
\]
where
\[
 H_{J,m}(j)=
 \left[1-\prod_{r=1}^J\left(1-\frac{j^2}{r^2}\right)\right]^m.
                                                               \tag{9}
\]
It is a nonzero polynomial of exact degree \(2Jm\), with leading
coefficient \((-1)^{m(J+1)}/(J!)^{2m}\).

Suppose the actual family is not identically one, and let \(k\geq1\)
be the first index for which the polynomial \(p_k\) in (1) is
nonzero. Put \(d=\deg p_k\). Equations (7)--(9) give
\[
 [h^a](\widetilde C_j(e^h)-1)=0\quad(a<k),\qquad
 [h^k](\widetilde C_j(e^h)-1)=H_{J,m}(j)p_k(j).     \tag{10}
\]
The polynomial on the right has exact degree \(d+2Jm\).
If
\[
 d+2Jm>2k,                                       \tag{11}
\]
then (1) rules out \(\widetilde C_j\), for all positive colors \(j\),
as the actual reduced zero-framed color family of any knot.
Equality of two proposed coefficient polynomials at every positive
integer \(j\) would be polynomial equality, so a higher-degree term
cannot be hidden by considering only integral colors.

For a fixed starting family with this nonzero \(p_k\), condition
(11) holds for sufficiently large \(m\) at any fixed \(J\geq1\).
This is an additional necessary source condition, beyond the finite
prefix, reciprocity, root-value bounds, and coherent normal-order
properties retained by B. It does not retract those properties.
If the starting family is identically one, the modification is
identically one and there is no first coefficient to test.

The conclusion concerns exactly (7). It does not exclude affine
repairs with additional terms matched to the perturbative expansion,
does not identify a geometric source coefficient, and gives no lower
bound at roots of unity or at a selected normal observation. No
uniform exchange of the small-\(h\) and large-color limits is made.

## 4. Complete proof-source pins

- A: [adequacy_and_algebraic_periods.md](adequacy_and_algebraic_periods.md),
  SHA256
  `d471549b23c1dd982b7152ef0e90d6fb51d1be9a3c73c1b52ed0e41c9b2c0caa`.
- B: [bounded_normal_color_transfer.md](bounded_normal_color_transfer.md),
  SHA256
  `6a464af6842c60b8c845d1dc52d8b3f7c105ce9e93c323a3c8bea4b04a6277dc`.

Both complete texts were read for this proof. The actual cut-source
facts used from A and the specific wall definition and regularity
used from B have been checked against those texts. The sharper
perturbative assertions mentioned in A are not proof premises here.
