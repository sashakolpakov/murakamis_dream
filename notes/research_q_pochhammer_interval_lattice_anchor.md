# The q-Pochhammer interval and its exact quantum-lattice anchor

Private written proof, 18 November 2026.

The ordinary infinite-product interval is an analytic interpolation of
each literal factorial or color product when the base has modulus less
than one. Its exact difference equation fixes every integer-lattice
restriction. Those restrictions continue as whole finite products to
roots of unity. The interpolation away from the lattice is not fixed
by integer pointing alone.

These are the standard q-Pochhammer functions, not new quantum
invariants: see [DLMF 17.2.1--17.2.4](https://dlmf.nist.gov/17.2#i).
The required convergence, difference identities, rigidity statements,
and source adapters are proved below. No special-function asymptotic
or summation theorem is used.

## 1. The analytic interval and its difference equation

In this note the product base is
\[
                        q=e^h,\qquad \operatorname{Re}h<0.
 \tag{1}
\]
It is the variable called \(Q\) in the literal crossing formulas
of [F]; their representation parameter is \(e^{h/2}\).
For \(|q|<1\), define
\[
             P(A;q)=\prod_{r=0}^{\infty}(1-Aq^r).
 \tag{2}
\]
This is entire in \(A\) and holomorphic jointly for \(|q|<1\).
Indeed on \(|A|\le M,|q|\le r<1\), the tail has
\(|Aq^j|\le1/2\), and its logarithm, expanded at one, is bounded
by \(2M\sum_{j\ge J}r^j\). Hence the tail converges normally to
a nonzero function; the finitely many initial factors retain every
zero. Reindexing the convergent product gives
\[
                       P(A;q)=(1-A)P(Aq;q).
 \tag{3}
\]

For a fixed integer offset \(c\), define the meromorphic interval
\[
       \Pi_c(h,s,Z)=\frac{P(Zq^c;q)}{P(Ze^sq^c;q)}.
 \tag{4}
\]
No logarithm of \(Z\) is required. The coordinate \(s\) is a
specified logarithmic endpoint, while (4) itself depends on \(e^s\).
Its exact row and pointing are
\[
 \boxed{\quad
 \Pi_c(h,s+h,Z)=(1-Ze^sq^c)\Pi_c(h,s,Z),
                         \qquad \Pi_c(h,0,Z)=1.
 \quad}
 \tag{5}
\]
They follow from (3). These are meromorphic identities. At an
intersection where numerator and denominator in (4) both vanish,
the restriction \(s=0\) means its canceled meromorphic restriction;
it does not assert holomorphy in all ambient directions there.

The factorial interval is the particular function
\[
 \mathfrak F(h,s)=\Pi_1(h,s,1)
           =\frac{(q;q)_\infty}{(e^{s+h};q)_\infty}.
 \tag{6}
\]
Its numerator is nonzero for \(|q|<1\), and
\(\mathfrak F(h,s+h)=(1-e^{s+h})\mathfrak F(h,s)\).
The original meridian \(Z\), when present in a color factor, is
retained as a variable throughout (4)--(5).

## 2. Pointed rigidity on the integer lattice

Define the whole finite or reciprocal product
\[
 (A;q)_L=
 \begin{cases}
  \prod_{r=0}^{L-1}(1-Aq^r),&L\ge0,\\
  \displaystyle\left[\prod_{r=L}^{-1}(1-Aq^r)\right]^{-1},&L<0.
 \end{cases}
 \tag{7}
\]
The empty product is one. Iterating (5) forward or backward gives
\[
                       \Pi_c(h,hL,Z)=(Zq^c;q)_L
                         \qquad(L\in\mathbb Z).
 \tag{8}
\]
For negative \(L\), this is a meromorphic identity in the free
parameters \((Z,q)\), with all reciprocal poles retained.
More generally any meromorphic solution of the row (5), defined
along the required shift orbit and pointed to one at zero, has
these same restrictions. The proof is finite induction, on the
open set where the factors are nonzero, followed by meromorphic
identity. It does not require asymptotics or Borel summation.

There is an essential specialization boundary. In (6), every
negative integer \(L\) makes the reciprocal product contain
\((1-q^0)^{-1}\). Thus that entire factorial lattice stratum is
polar; it has no finite meromorphic-in-\(h\) value. Formula (8)
does not assign a negative factorial to it. The actual supported
Gaussian coefficients below use only nonnegative factorial lengths.

For \(L\ge0\), the right side of (8) is polynomial in \(Z\)
and Laurent polynomial in the nonzero base \(q\). Consequently
the restricted function has a unique continuation to every root
of unity, with its literal finite-product value. This statement
first restricts and cancels the whole interval; it does not take
boundary values of the two infinite products separately. For
negative \(L\), the analogous continuation is meromorphic, with
exactly the reciprocal denominator specified in (7), unless
additional factors in a larger whole expression cancel it.

## 3. Both actual crossing signs and whole Gaussian cancellation

For nonnegative \(A\) and \(0\le n\le A\), form
\[
 G_{A,n}(q)=\frac{(q;q)_A}{(q;q)_n(q;q)_{A-n}}.
 \tag{9}
\]
Away from the displayed zeros, elementary cancellation gives
\[
 G_{A,n}=G_{A-1,n-1}+q^nG_{A-1,n},
 \qquad G_{A,0}=G_{A,A}=1.
 \tag{10}
\]
Indeed the two ratios to the left side of (9) are respectively
\((1-q^n)/(1-q^A)\) and
\(q^n(1-q^{A-n})/(1-q^A)\), whose sum is one. Induction proves
that (9), as a whole rational expression, is a polynomial in
\(q\). Its polynomial value, rather than three separately
specialized factorials, is therefore the value at every root.

To check the actual source adapter, use the original indices
\(a,b,n\) and the independent meridian \(x\) of [F]. The
supported entries, with the base named as in (1), are
\[
\begin{split}
 R^+_{b+n,a-n;\,a,b}
   &=x^{-a-b+n}q^{(a-n)b}G_{a,n}(q)
                    (x^{-2}q^{a-n};q)_n,
                        &&0\le n\le a,\\
 R^-_{b-n,a+n;\,a,b}
   &=x^{a+b-n}q^{-ab}G_{b,n}(q)
                    (x^2q^{1-b};q)_n,
                        &&0\le n\le b.
\end{split}
 \tag{11}
\]
Put \(Y=qx^2\). Their two color products are exactly
\[
                 (Y^{-1}q^{a-n+1};q)_n,
                 \qquad (Yq^{-b};q)_n.
 \tag{12}
\]
Thus each is an instance of (8), without replacing any peripheral
factor by its value at a special meridian. For example the upper
one is \(\Pi_1(h,hn,Y^{-1}q^{a-n})\), and the lower is
\(\Pi_0(h,hn,Yq^{-b})\). Both match the same original support;
no off-support or negative factorial value is added.

Equations (8)--(12) prove exact entrywise lattice matching and
whole-entry continuation to all roots for \(x\ne0\). The ordinary
pivot \(q^{-\sum a_i}\), scalar framing \(x^{c_\beta}\), where
\(c_\beta=b_\beta-1-w_\beta\), matching equations,
and highest cut of [F] are left untouched. Finite algebraic
combinations of such entries inherit these identities. This does
not justify any untruncated sum, trace, or Gaussian integral.

## 4. Comparison with the exact Euler coefficients

There is a direct comparison with [D]'s actual formal defect.
First take \(|Z|,|Ze^s|<1\), and initially \(h\) small in
\(\operatorname{Re}h<0\), so the logarithms continued from
\(Z=0\) have the absolutely convergent expression
\[
 \log\Pi_c(h,s,Z)
   =\sum_{m\ge1}
      \frac{Z^m(1-e^{ms})e^{cmh}}{m(e^{mh}-1)}.
 \tag{13}
\]
This follows by expanding each factor's logarithm and summing its
geometric \(q\)-tail. For negative fixed \(c\), first require
\(|Zq^c|,|Ze^sq^c|<1\); these inequalities hold on smaller
compact \(Z,s\) sets for sufficiently small \(h\).

Expand (13) formally in \(h\), coefficientwise first in \(Z\),
using the Bernoulli generating germ. If
\(F_Z(t)=\log(1-Ze^t)\), the result is precisely
\[
 h^{-1}\int_0^sF_Z(t)\,dt
  +\sum_{a\ge1}h^{a-1}\frac{B_a(c)}{a!}
          \bigl(F_Z^{(a-1)}(s)-F_Z^{(a-1)}(0)\bigr).
 \tag{14}
\]
For each fixed order the \(m\)-series converges normally on the
smaller \(Z,s\) domain, since its growth is polynomial in \(m\).
This is a formal coefficient comparison; it does not interchange
an infinite \(h\)-series with (13).

The normalized color function of [D] is
\(F_Z(t)-F_Z(0)\). Therefore its defect in (14) is unchanged,
while the principal term separately retains
\((s/h)\log(1-Z)\). In particular the entire peripheral factor
\((1-Z)^L\) is retained on the integer lattice. The formal defect
has exactly the continued Borel germ \(\widehat V_c\) of [D],
with its two endpoint branches and constant term. The coefficient
identity continues on the same logarithmic endpoint charts.

For the factorial specialization, the lower endpoint of
\(\log(1-e^t)\) is singular and must not be substituted into
(14). At a nonnegative integer length instead use the exact
finite identity
\[
 (q;q)_L=(-h)^L L!\,
      \exp\left\{\sum_{r=1}^L F_0(hr)\right\},
          \qquad F_0(t)=\log\frac{e^t-1}{t},
 \tag{15}
\]
with the logarithms continued from \(h=0\) in the unit factors.
The remaining analytic interval has precisely [D]'s \(c=1\)
defect and original endpoint at zero. Classical \((-h)^L L!\)
and any logarithmic marks are not absorbed into it. Extending
those separate classical factors off the integer lattice requires
its own normalization; (15) makes no silent Gamma interpolation.

These calculations identify the formal Euler data attached to the
pointed interval. They do not prove that a chosen finite or infinite
Laplace transform of [D] equals (4), nor that an arbitrary continued
Borel branch has the infinite product's normalization. An exact
remainder or analytic summation argument would be needed for that
stronger assertion.

## 5. What integer pointing fixes, and what it cannot fix

Fix \(h\) with \(\operatorname{Re}h<0\), and generic parameters
where the interval is nonzero. If \(A(s)\) is another meromorphic
solution of (5), its quotient
\[
                         H(s)=A(s)/\Pi_c(h,s,Z)
 \tag{16}
\]
satisfies \(H(s+h)=H(s)\) as a meromorphic identity. Conversely
every such periodic quotient gives another solution. Pointing is
exactly \(H(0)=1\), and then
\[
                              H(hL)=1\quad(L\in\mathbb Z)
 \tag{17}
\]
where these restrictions exist. On the full \(s\)-plane a periodic
meromorphic function descends to a meromorphic function of
\(w=e^{2\pi i s/h}\) on \(\mathbb C^*\): local logarithm
choices differ by integer multiples of \(h\). Thus integer
pointing only fixes its value at \(w=1\), not its values elsewhere.
This is the exact ambiguity in the actual interval difference
equation, not a change of its integer products.

There is a simple additional condition satisfied by (4) that does
remove the ambiguity. It descends to \(a=e^s\) and is holomorphic
at \(a=0\), with value \(P(Zq^c;q)\). If the quotient of two
solutions descends to \(a\) and is meromorphic at \(a=0\), then
\[
                         H(qa)=H(a)
 \tag{18}
\]
forces it to be constant. Indeed its convergent Laurent expansion
there has coefficients \(H_k\) satisfying
\((q^k-1)H_k=0\); since \(|q|<1\), only \(k=0\) remains.
Pointing then makes the constant one, and meromorphic continuation
gives equality on the connected domain. The proof is first on the
generic parameter set and hence preserves all meromorphic identities.

Equivalently, (4) is selected by its exact tail normalization
\[
             \lim_{N\to\infty}\Pi_c(h,s+Nh,Z)=P(Zq^c;q).
 \tag{19}
\]
Any solution of (5) with that same limit satisfies
\[
 A(s)=\frac{\lim_{N\to\infty}A(s+Nh)}
                    {\prod_{r\ge0}(1-Ze^sq^{c+r})}
                 =\Pi_c(h,s,Z),
 \tag{20}
\]
initially away from zeros and then meromorphically. The regularity
or tail condition is genuinely additional to the integer values.

There is also no periodic ambiguity inside a formal power series
\(H(h,s)=\sum_{j\ge0}h^jH_j(s)\) with coefficients holomorphic
near \(s=0\), if the shift identity and pointing hold formally.
The first shift coefficient gives \(H_0'=0\). Inductively, once
the earlier coefficients are constant, the next gives \(H_j'=0\).
The pointing sets \(H_0=1\) and \(H_j=0\) for \(j>0\).
Punctured analytic functions depending on \(e^{2\pi i s/h}\)
need not belong to this formal class. Formal uniqueness therefore
does not identify all analytic interpolations.

## 6. Exact scope and complete proof sources

The infinite-product interpolation has the original scalar lattice
values and all-root whole-product restrictions. Its formal defect
coefficients agree with the original Euler calculation. The additional
tail normalization specifies its off-lattice analytic choice. None
of these facts alone identifies it with an arbitrarily selected
Borel--Laplace branch or with an assembled knot period.

In particular the signed untruncated source has factors such as
\(q^{(a-n)b}\) and \(q^{-ab}\). At \(|q|\ne1\), scalar interval
convergence gives no permission to interchange their infinite index
sum with Gaussian operations or closure. The original highest-cut
trace, full relative cycle, and physical finite invariant remain
separate analytic comparisons. No such interchange or invariant
identity is claimed here.

The existing private notes on fixed-root factorial interpolation and
on unfolded Ward factorials cover other exact lattice constructions.
They are coverage only. The present comparison retains the moving
base, the literal interval equation, and [D]'s Borel convention;
the special-function definition itself carries no novelty claim.

| Label | Complete proof source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| D | notes/research_literal_interval_global_borel_log.md | d0885ed0ae7f050ad72d8d128a1edb7bef4200f1b02f624612a8946bbef72a2e |

F supplies the literal signed entries and retained cut normalization;
D supplies their exact formal interval and Borel defect conventions.
Both complete texts were read and all used implications checked.
All infinite-product, difference, root-extension, and ambiguity proofs
are above. The linked DLMF page is definition coverage only.
No mathematical program, test, build, or imported asymptotic proof was
used. Frozen notes and public manuscripts are unchanged.
