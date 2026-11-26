# Real conditional roots and a uniform left contour

Research proof, 4 November 2026. This note supplies contour geometry for
the original conditional phase on every compact real parameter set in
\((0,1/2)^2\). It does not evaluate the complete conditional sum. In
particular the high half of the index range is not discarded or bounded
by a norm. Frozen manuscripts and completed source artifacts are unchanged.

## 1. Original phase and selected root

Use
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\qquad
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,
 \quad \epsilon\in\{0,1\}.                                      \tag{1}
\]
Throughout this note \(0<a,b<1/2\) are real. All values with
\(0<\Re s<1/2\) use the original regular-strip logarithms. At the
left boundary, values are limits from \(\Re s>0\).

Put \(P=\cot\pi a>0,\ Q=\cot\pi b>0\). The
[global root theorem](research_mixed_global_cotangent_roots.md) gives a
unique simple original zero-lift root \(s_*=x_*+ih_*\) with
\[
 S_*:=\cot\pi s_*=u+iv,\qquad u>0,\quad |v|<1.                 \tag{2}
\]
These roots and all their derivatives stay in compact regular sets when
\((a,b)\) ranges over a compact subset of \((0,1/2)^2\). They are
specified analytically, with no numerical root-count premise.

## 2. An exact upper-height bound for type four

**Lemma 1.** For \(\epsilon=1\), every real-parameter root (2) obeys
\[
 e^{2\pi h_*}<\sqrt2.                                         \tag{3}
\]

Write \(p=P,q=Q\). The cubic is
\(F=(S+i)(S+p)(S+q)-2i(p-i)(q+i)\). Since
\[
 e^{4\pi h_*}=\frac{u^2+(v-1)^2}{u^2+(v+1)^2},
\]
equality in (3) is the circle
\(u^2=-v^2-6v-1\), with \(-1<v<0\). On this circle,
\[
 \Im F=-4v^3-20v^2-9v-3+u(p+q)(2v+1)+pq(v-1).               \tag{4}
\]
If \(v\le-1/2\), put \(v=-1/2-t\), \(0\le t<1/2\). The
first term becomes \(4t^3-14t^2-8t-3<0\), and the remaining
terms are nonpositive. No root is possible there.

For \(-1/2<v<0\), solve the cubic for \(q\):
\[
 Dq=Z,\quad D=(S+i)(S+p)-2i(p-i),\quad
 Z=-S(S+i)(S+p)-2(p-i).
\]
Reducing modulo the circle equation gives
\[
 \frac18\Im(Z\overline D)=A p^2+Bp+C,\quad
 A=v(v+2),\quad B=u(2v+1)(v+1),\quad
 C=-(2v+1)(2v^2+2v+1).                                      \tag{5}
\]
Here \(A<0\), and its discriminant is
\[
 B^2-4AC=-(2v+1)T(v),\quad
 T(v)=2v^5+9v^4+12v^3+10v^2+2v+1>0.                         \tag{6}
\]
Indeed, with \(w=v+1/2\in(0,1/2)\),
\(T=2w^5+4w^4+(3w^2-w^3)+(3/2-23w/8)>0\); its last term is
at least \(1/16\). Thus (5) is strictly negative for every real
\(p\). At a root with real \(q\), however,
\(\Im(Z\overline D)=\Im(q|D|^2)=0\). This also excludes
\(D=0\), without division by an unproved nonzero quantity.

The selected root therefore cannot cross the circle. At \(P=Q=1\)
the rational Rouché disk in the global root theorem has \(v>0\),
so (3) holds there. Connectedness of the positive real parameter
quadrant proves (3) everywhere. This proof uses only exact polynomial
identities and sign inequalities.

## 3. The whole left-half horizontal maximum

**Theorem 2.** For either type and every real \(a,b\in(0,1/2)\),
\[
 \Re Q_\epsilon(x+ih_*;a,b)<\Re Q_\epsilon(s_*;a,b)=:M
 \quad(0\le x\le1/2,\ x\ne x_*).                            \tag{7}
\]
The maximum is nondegenerate. All strict gaps away from a fixed
neighborhood of the root are uniform on compact real parameter sets.

For a fixed height \(h\), define
\[
 L(h)=\frac1{2\pi}\arccos(e^{-2\pi|h|}).                     \tag{8}
\]
The inverse image of the inner cotangent cone on that horizontal line
is precisely \(L(h)<x<1/2\). Throughout this interval the
triangle-form determinant from
[plateau accretivity](research_mixed_plateau_accretivity.md) is positive:
the outer cotangents are positive real, while the inner cotangent has
positive real part and imaginary part of magnitude less than one.
The two triangle forms, plus the extra type-four own-index term, give
\(-\Re Q_{ss}>0\). Hence the real phase is strictly concave on this
interval. Its unique critical point at height \(h_*\) is \(x_*\).

It remains to control \(0\le x\le L(h_*)\). Put
\(R=e^{2\pi h_*}\), \(U=R e^{-2\pi ix}\). For
\(0\le x\le1/4\) and \(0<a<1/2\),
\(\sin^2\pi(x+a)>\sin^2\pi x\). Therefore
\[
 |1-e^{-2\pi ia}U|>|1-U|,
 \qquad |1-e^{-2\pi ib}U|>|1-U|.                             \tag{9}
\]
For type three, (9) directly gives \(\Re Q_s>0\). For type four
one additionally needs \(|1-U|<1\). If \(h_*<0\), the low-arc
condition gives \(\cos2\pi x\ge R\), so
\(|1-U|^2\le1-R^2<1\). If \(h_*>0\), it gives
\(\cos2\pi x\ge R^{-1}\), so
\(|1-U|^2\le R^2-1<1\) by Lemma 1. At zero height the low arc
has length zero. The original equation
\[
 \Re Q_s=
 \log\frac{|1-e^{-2\pi ia}U|\,|1-e^{-2\pi ib}U|}
 {|1-U|^{2+\epsilon}}                                      \tag{10}
\]
now proves strict increase on the whole low arc. It joins the strict
concave maximum in the cone, proving (7). The endpoint limits at
\(x=0\) and \(x=1/2\) are retained by continuity.

For type three this horizontal conclusion also extends through the
entire original physical support \(0\le x\le1-\max(a,b)\):
on its portion \(x\ge1/2\), each shifted sine modulus is at most
the unshifted one, so (10) is strictly negative. This extra statement
does not control the associated vertical endpoint currents.

## 4. The left endpoint, its initial rows, and both aliases

**Lemma 3.** At \(s=iy+0^+\), the real phase is strictly increasing
away from \(y=0\), in either direction. Consequently
\[
 \max_{y\text{ between }0\text{ and }h_*}
       \Re Q_\epsilon(iy+0^+;a,b)
 =\Re Q_\epsilon(ih_*+0^+;a,b)<M.                            \tag{11}
\]

For \(y<0\), \(g'(iy)\) is real and each
\(\arg(1-e^{2\pi y-2\pi ia})\) is positive. Thus
\[
 \frac d{dy}\Re Q_\epsilon(iy+0^+)
 =-\arg(1-R e^{-2\pi ia})-\arg(1-R e^{-2\pi ib})-2\pi a<0.
\]
For \(y>0\), the right-boundary lift has \(\Im g'(iy+0^+)=\pi\).
For \(R>1\) and \(0<a<1/2\),
\(0<\arg(1-R e^{-2\pi ia})<\pi-2\pi a\). Therefore
\[
 \frac d{dy}\Re Q_\epsilon(iy+0^+)
 >(2+\epsilon)\pi-2\pi a-(\pi-2\pi a)-(\pi-2\pi b)
 =\epsilon\pi+2\pi b>0.                                    \tag{12}
\]
The boundary phase is continuous at zero. Theorem 2 supplies the final
strict inequality in (11).

Fix any compact \(K\Subset(0,1/2)^2\). Compactness in (7) and (11)
gives a uniform left-endpoint gap. Consequently one may choose a single
small \(l>0\), depending on \(K\), so that all selected-side joins
\(l+i[0,h_*]\) have a strict gap. On the real interval near zero,
\(\partial_s\Re Q=-(2+\epsilon)\log s+O_K(1)\). Thus \(l\)
can also be chosen so that the complete initial real tail increases to
\(l\), where its rate remains below \(M\). To see the finite-row
bound explicitly, write \(P_j=\prod_{k=1}^j(1-r^k)\),
\(r=e^{-2\pi i/N}\). For \(j\le lN\), the shifted product logarithms
at \(a+k/N\) and \(b+k/N\) are smooth on fixed compact subintervals
of \((0,1)\); their sum-minus-integral errors are uniformly bounded.
For the unshifted product, isolate \(\log(k/N)\) from
\(\log(2\sin(\pi k/N))\). Stirling's inequality and the smooth
remainder give a uniform \(O(\log N)\) error, including \(j=0\).
Consequently each original physical row has
\(\log|\mathcal T_N(j/N)|\le N\Re Q_\epsilon(j/N)+C_K\log N\).
This controls every initial row with only a polynomial level factor.
Half-grid rounding of the fixed positive cut preserves the gaps.

The exact reflection identity on \(0\le x\le1/2\) is
\[
 \Re Q_\epsilon(x-iy)-\Re Q_\epsilon(x+iy)
 =2\pi y\{a-b+\epsilon(x-1/2)\}.                            \tag{13}
\]
On \(K\), the absolute value of the braces is bounded by a fixed
\(\Lambda_K<1\). This retains the original chirp and gives both
cotangent aliases a gain of at least
\(2\pi(1-\Lambda_K)|y|\) relative to the opposite selected-side
phase. In particular all left vertical alias currents inherit the
strict endpoint gap.

For horizontal aliases choose heights
\(\pm Y\), \(Y=|h_*|+\tau\). On \([l,1/2]\), the uniform
nondegenerate maximum (7) and analytic Taylor bounds give a selected-side
upper rate \(M+C_K\tau^2\) for sufficiently small fixed \(\tau>0\).
Away from the root, use its compact strict gap; near it, complete the
quadratic bound. Reflection (13) and the literal cotangent remainder
\(O(e^{-2\pi NY})\) give the rate
\[
 M+C_K\tau^2-2\pi(1-\Lambda_K)Y<M
 \quad\hbox{if }C_K\tau<2\pi(1-\Lambda_K).                  \tag{14}
\]
This also treats \(h_*=0\), with \(Y=\tau\). The exact zero mode
remains \(+N\int\mathcal T_N(s)\,ds\); no residue or alias is
removed by these phase estimates.

## 5. What remains for a complete source theorem

The right join at \(\Re s=1/2\) is not disposed of here. Its real
endpoint can exceed \(M\), even when the whole horizontal line through
the root is controlled. Thus the high-half rows must in general be
deformed coherently with the low half. A proof still needs the actual
factorial continuation across its shifted walls, the full high-half
comparison and the resulting endpoint and alias exhaustion. Neither
root uniqueness nor (7) proves those assertions. No complete-sum
nonvanishing or whole-period asymptotic is claimed.

Reproduction:

    python3 experiments/check_mixed_real_conditional_contour_geometry.py --precision 256

The checker verifies the polynomial height exclusion and the phase
identities exactly. The analytic monotonicity and compactness arguments
above provide the inequalities; no sampled maximum enters acceptance.
