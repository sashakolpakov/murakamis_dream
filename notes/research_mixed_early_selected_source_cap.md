# Conditional sums with an earlier positive selected height

Research note, 4 November 2026. The complete boundary cover proves the
finite-sum estimate below on the enlarged transition domains. The
estimate includes both neighboring parameters independently; it does
not yet control the remaining outer integral.

An earlier rise of the selected contour requires height \(.014\)
at real coordinates below \(.22\). The existing transition theorem
only permits a positive height proportional to \(x-.1\). This note
sets out a separate source estimate for the larger domain. It does not
prove that the proposed contour has a global phase gap.

## 1. The enlarged domains and the literal sum

Put \(H=7/500\), and define
\[
 \begin{split}
 T_3&=\operatorname{conv}\{.1,\ .22-.03i,\ .22+.02i\},\\
 T_4^+&=\operatorname{conv}\{.1,\ .22-.057i,\ .22+Hi,\ .12+Hi\},\\
 B_3&=[.22,.45]+i[-.03,.02],\qquad
 B_4=[.22,.45]+i[-.057,H].
 \end{split}                                                   \tag{1}
\]
Write \(T_4=T_4^+\) in the typed products below. The lower boundary
of the type-four triangle is unchanged. Its upper boundary rises
linearly from zero at \(.1\) to \(H\) at \(.12\), then remains
horizontal. This contains the full proposed early selected rise.

Use the marked factorial continuation \(P_N\) and the original
canonical finite function from
[the complete transition source theorem](research_mixed_transition_whole_period_source.md):
\[
 L_{\epsilon,N}(a,b)
 =\sum_{j=0}^{N-1}e^{2\pi iaj}
       \frac{P_N(Na+j)P_N(Nb+j)}{P_N(j)^{2+\epsilon}}.
                                                               \tag{2}
\]
Here \(\epsilon\in\{0,1\}\) is the type of the second argument
minus three. The type of the first argument is denoted \(\eta\).
The phase is
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,
 \quad
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
                                                               \tag{3}
\]
with the original logarithmic branch on the regular strips. Let
\(s_*(a,b)\) be its original zero-lift critical root. Define
\[
 a_0(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2},\qquad
 A_\epsilon(a,b)=
 \frac{\sqrt{2\pi}\,a_0(s_*+a)a_0(s_*+b)}
      {a_0(s_*)^{2+\epsilon}\sqrt{-Q_{\epsilon,ss}(s_*)}}.
                                                               \tag{4}
\]
The square roots are the branches fixed by the preceding source theorem.

**Theorem 1.** On every ordered product \(T\times T\),
\(T\times B\), and \(B\times T\) of the indicated types is
\[
 L_{\epsilon,N}(a,b)
  =N^{(1-\epsilon)/2}A_\epsilon(a,b)
         e^{NQ_\epsilon(s_*;a,b)}(1+O(N^{-1})).                \tag{5}
\]
The estimate is uniform on a fixed open neighborhood of each closed
product, with all fixed parameter derivatives on smaller neighborhoods.
The corresponding literal conditional polynomial is
\(C_{\epsilon,N}=L_{\epsilon,N}/[P_N(Na)P_N(Nb)]\), so its
power of \(N\) is \(-(1+\epsilon)/2\), its action is
\(Q_\epsilon(s_*)-g(a)-g(b)\), and its symbol is
\(A_\epsilon/[a_0(a)a_0(b)]\).

## 2. The geometric branch exists on the enlarged domain

For the new positive cap, \(.1\le x\le.45\) and \(0\le h\le H\).
The elementary formula for the imaginary part of the cotangent gives
\[
 |\Im\cot\pi(x+ih)|
 =\frac{\sinh(2\pi h)}{\cosh(2\pi h)-\cos(2\pi x)}
 \le\frac{\sinh(7\pi/250)}{2\sin^2(\pi/10)}<\frac12.          \tag{6}
\]
The final strict inequality is an outward scalar comparison. The
negative part of the domain has the old ramp bound from the
[minimum-neighbor polygon theorem](research_mixed_minimum_neighbor_contour.md).
The unchanged type-three domain has that bound as well. Also the real
part of the cotangent is positive, since all real coordinates are
strictly between zero and one half.

The global cotangent theorem therefore gives a unique holomorphic
zero-lift root on a neighborhood of each product in (1). Its three
factorial arguments stay in their regular strips, and the real part
of \(-Q_{\epsilon,ss}\) is positive. Thus the action and the
nowhere-zero symbol (4) are well defined before a finite-sum estimate
is attempted.

## 3. Boundary estimates and proof of Theorem 1

There are \(49\) edge products of type \(T\times T\), and \(56\)
each of types \(T\times B\) and \(B\times T\). The total is
\(161\). The checker covers all of them; none is inferred from
values on a finite grid or from the old triangular domain.

On each product it checks the following sufficient conditions from
Sections 2--4 of the complete transition source theorem:

* The polynomial controlling the derivative on the high half of the
  horizontal contour has \(G(w)=wF'(w)-2F(w)>0\) on
  \([0,\infty)\), including a positive leading coefficient.
  Compactification and subdivided Bernstein coefficients prove this
  on the whole interval.
* The selected action has positive real part, and both endpoints of
  the full horizontal contour lie at least \(10^{-4}\) below it.
* All four alternatives in the exact right-midpoint multiplier lie
  at least \(10^{-4}\) below the selected action.
* The exceptional type-four positive vertical profile, maximized over
  its entire height interval \([0,2]\), has the same strict gap.

Every root is enclosed by an original-logarithm Newton self-map. The
coefficient and endpoint bounds retain the derivative of the critical
height with respect to both outer parameters. Exact dyadic covers
account for every boundary parameter. Saved-cover replay uses rational
witnesses, with no new root or maximum proposals.

The complete cover has 71,240 accepted dyadic cells in 161 products.
All the inequalities above are strict on every cell. The computation
also verifies eleven exact identities and three scalar inequalities,
including (6) and the two remote-horizontal bounds. These are the
finite inequalities used in the following argument.

**Proof.** The left-half circle argument and the polynomial condition
give the unique full-horizontal maximum at \(s_*\), with the stated
endpoint gaps. The midpoint identities retain all finite rows and all
numerator multipliers. Their vertical contributions are controlled by
the four branch inequalities and the exceptional concave profile.
The two remote horizontals still have heights \(\pm2\); their
original bounds apply because \(-.057\le\Im a,\Im b\le.02\)
and \(.1\le\Re a,\Re b\le.45\) are unchanged.

The exact cotangent residue formula therefore leaves the original
zero-mode coefficient \(+N\) and its nondegenerate Gaussian integral.
Near a vanishing shifted height, move the far horizontal slightly
away from the three real factorial axes, while the central segment
passes through the saddle inside its regular strips. The strict gaps
persist on the connecting pieces. This gives (5) on a neighborhood
of the product boundary using the existing factorial expansions.

The normalized error in (5) is holomorphic in both outer parameters.
Two maximum principles extend its boundary bound through the complete
product. Compactness and Cauchy estimates give the stated neighborhoods
and parameter derivatives. No branchwise positivity test is itself
continued by a maximum principle. \(\square\)

Together with the existing full plateau-square packet, this gives
the same asymptotic on the independent polygon products
\((T_{3+\eta}\cup B_{3+\eta})\times(T_{3+\epsilon}\cup B_{3+\epsilon})\).
It supplies the source for a selected contour rising earlier. It
does not prove a supporting-plane bound, a noncancelling outer
contribution, or a new knot theorem.

## 4. Reproduction

```sh
python3 experiments/certify_mixed_early_selected_source_cap.py --precision 256
```

The saved record contains every dyadic cell and its rational root
witness. To check those same cells at higher precision, without new
root proposals or further subdivisions, run:

```sh
python3 experiments/certify_mixed_early_selected_source_cap.py \
  --precision 320 \
  --input repro/results/research-mixed-early-selected-source-cap.json \
  --output /tmp/research-mixed-early-selected-source-cap-replay.json
```
