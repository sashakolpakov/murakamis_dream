# An analytic upper bound for the complete half-cap action

Research deduction, 7 November 2026. The original half-cap action
satisfies \(M_{\rm half}<203/200\). We first prove a \(51/50\)
ceiling and then sharpen its elementary real-primitive bound.
The argument retains the decrease
from the positive real-row profile to the negative critical
height. It uses only the already saved endpoint scalar, the
proved original critical branch, and elementary inequalities.
No root, action, derivative, or certificate is evaluated again.

The result is a scalar upper bound for the actual complete-cap
action. It is not a comparison of the cap--conditional product
with the next-source affine action.

## 1. Original action and saved scalar input

Use the exact source, phase, and critical point of
[the complete half-cap theorem](research_mixed_half_face_complete_cap_packet.md):
\[
 \begin{gathered}
 \Psi(e)=S(e)+J(e+1/2)-J(1/2)-i\pi e/2,\qquad
 \Psi_e(e_+)=0,\\
 M_{\rm half}=\Re\Psi(e_+),\qquad e_+=x_++ih_+,\\
             \frac{17}{50}<x_+<\frac7{20},
                 \qquad -\frac1{20}<h_+<0.
 \end{gathered}                                                     \tag{1}
\]
These refer to the original endpoint sheet and zero logarithmic
lift, with all additive constants fixed.

Write \(\lambda(x)=\Re S(x)\) on the real interval.
The original
[seam source replay](../repro/results/research-mixed-cap-seam-source-bounds-replay.json),
SHA256
8d907c890073955f7e1122abc78f1334ab00a885959d839316d3852e2a64f3f8,
records the full outward enclosures beginning
\[
 \begin{split}
 \lambda(7/20)&=
 [\,0.864089941023120636\ldots\ \mathord\pm1.37\,10^{-94}\,],\\
 \lambda'(7/20)&=
 [\,-0.004747972220743908\ldots\ \mathord\pm5.18\,10^{-95}\,].
 \end{split}                                                       \tag{2}
\]
Their exact saved displays directly imply
\[
       \lambda(7/20)<\frac{8641}{10000},\qquad
                -\frac1{200}<\lambda'(7/20)<0.                    \tag{3}
\]
Only these rational consequences of the existing record are used.
The original real-index curvature gives \(\lambda''<0\).
Its supporting tangent at \(7/20\), evaluated throughout (1), yields
\[
                 \lambda(x_+)<\frac{8641}{10000}
                           +\frac1{20000}
                            =\frac{17283}{20000}.                \tag{4}
\]

Since \(3/20<1/2-x_+<4/25<1/6\), sine concavity gives
\(2\sin(\pi s)\ge6s\) on the relevant interval. Therefore
\[
 -J(1/2-x_+)
    \le v(1-\log(6v))<\frac16,\qquad v=1/2-x_+.
                                                                    \tag{5}
\]
Here \(v(1-\log(6v))\) increases up to \(v=1/6\).
Oddness about one half and \(J(1/2)=0\) now imply the real-row bound
\[
                     \Re\Psi(x_+)
                       <\frac{17283}{20000}+\frac16.             \tag{6}
\]

## 2. The critical depth has a fixed lower bound

Keep the cubic's unique real root \(\alpha\). The complete
half-cap proof gives \(\alpha<3/14\) and the exact relation
\[
                 |e^{2\pi i e_+}|^2
                       =\frac4{1+4\alpha+7\alpha^2}
                       >\frac{112}{61}.                         \tag{7}
\]
Thus
\[
 |h_+|>\frac{\log(112/61)}{4\pi}
       >\frac{102}{173}\frac7{88}
        =\frac{357}{7612}>\frac3{64}.                             \tag{8}
\]
The middle inequalities use
\(\log u>2(u-1)/(u+1)\) and \(\pi<22/7\).
The final cross-product difference is
\(357\cdot64-3\cdot7612=12>0\).
In particular (8) retains a quantitative depth, rather than
only the sign of the critical height.

## 3. Vertical curvature greater than ten

We prove on the full small rectangle
\[
       17/50\le x\le7/20,\qquad -1/20\le h\le0,\qquad e=x+ih,
                                                                    \tag{9}
\]
that
\[
                           -\Re\Psi_{ee}(e)>10.                  \tag{10}
\]
The original exact identity is
\[
 -\Psi_{ee}(e)=
       \frac{2\pi}{\sin(2\pi e)}
       +\frac{2\pi}{\sin(\pi e)\sqrt{2-e^{-2\pi ie}}}.
                                                                    \tag{11}
\]
Both denominators retain the original branches.

First put \(s=\sin(2\pi x)\) and \(q=|\sinh(2\pi h)|\).
The exact half-angle values and elementary positive-series
bounds give
\[
             \frac45<s<\frac{\sqrt3}{2},\qquad 0\le q<\frac13.
                                                                    \tag{12}
\]
For the hyperbolic bound, the series implies
\(\sinh z\le z/(1-z^2/6)\) when \(0\le z^2<6\).
As \(2\pi|h|\le\pi/10<11/35\), its upper bound is
\(2310/7229<1/3\).
The sine bounds follow from
\(2\pi x\in[17\pi/25,7\pi/10]\subset(2\pi/3,7\pi/10]\)
and \(\sin(3\pi/10)=(1+\sqrt5)/4>4/5\).

The real reciprocal is
\[
 \Re\frac1{\sin(2\pi e)}
           =\frac{s\sqrt{1+q^2}}{s^2+q^2}.
                                                                    \tag{13}
\]
On (12), this expression decreases in both \(s\) and \(q\).
For the first derivative the sign is that of \(q^2-s^2<0\);
for the second it is that of \(s^2-2-q^2<0\), with the
zero derivative at \(q=0\) interpreted by continuity.
Consequently
\[
 \Re\frac1{\sin(2\pi e)}
        >\frac{6\sqrt{30}}{31}>\frac{32}{31}.                    \tag{14}
\]
The last inequality follows from \(30>(16/3)^2\).

For the second denominator of (11), the smaller hyperbolic
argument gives \(|\sinh(\pi h)|<1/6\). Indeed the same series
at \(11/70\) gives \(4620/29279<1/6\).
Also
\[
              \sin(\pi x)\le\cos(3\pi/20)<\frac9{10}.
                                                                    \tag{15}
\]
One direct witness for (15) uses \(3\pi/20>15/32\):
for \(0\le v\le1\), the cosine upper polynomial gives
\(\cos v\le1-11v^2/24\), and
\(11(15/32)^2/24=2475/24576>1/10\).
Hence
\[
 |\sin(\pi e)|^2<\frac{81}{100}+\frac1{36}
          =\frac{377}{450}<\frac{121}{144},
                \qquad |\sin(\pi e)|<\frac{11}{12}.              \tag{16}
\]
Since \(|e^{-2\pi ie}|\le1\), the other factor obeys
\[
             \left|\sqrt{2-e^{-2\pi ie}}\right|
                        \le\sqrt3<\frac74.                       \tag{17}
\]
The argument bounds in the complete half-cap proof apply on
(9): \(\arg\sin(\pi e)\in(-11/70,0]\) and
\(\arg\sqrt{2-e^{-2\pi ie}}\in(0,1/4)\).
Thus the product's argument has modulus less than \(1/4\).
Using \(\cos(1/4)>31/32\), (16)--(17) imply
\[
 \Re\frac1{\sin(\pi e)\sqrt{2-e^{-2\pi ie}}}
     >\frac{31}{32}\frac{48}{77}
      =\frac{93}{154}>\frac35.                                  \tag{18}
\]
Combining (11), (14), and (18), and using \(\pi>25/8\), proves
\[
 -\Re\Psi_{ee}
       >2\pi\left(\frac{32}{31}+\frac35\right)
        =\frac{506\pi}{155}>\frac{1265}{124}>10.
                                                                    \tag{19}
\]

## 4. The actual action ceiling

Set \(f(h)=\Re\Psi(x_++ih)\). The original critical equation gives
\(f'(h_+)=0\), while (10) gives \(f''(h)>10\) throughout
\([h_+,0]\). Integrating twice gives
\[
                f(0)-f(h_+)>5h_+^2>\frac{45}{4096}.             \tag{20}
\]
This is the decrease from the real profile to the original
complex critical point; no freely selected phase is substituted.

Equations (6) and (20) prove the strict bound
\[
 \boxed{\quad
 M_{\rm half}
   <\frac{17283}{20000}+\frac16-\frac{45}{4096}
    =\frac{51}{50}-\frac{1303}{7680000}
    <\frac{51}{50}.
 \quad}                                                         \tag{21}
\]
It concerns the same absolute action and the same nonzero whole
cap expansion as the complete half-cap theorem. By strictness
and the proved holomorphic action germ, the ceiling \(51/50\)
persists on a sufficiently small fixed complex neighborhood of
\((a,w)=(1/2,-2)\). This continuation preserves the original
source, implicit critical branch, and normalized derivatives;
it does not extend the outgoing real interval to \([.5,.7]\).

The complete-cap all-real angular upper bound can likewise use
(21) at \(a=1/2\), with its existing polynomial factors and fixed
ordinary derivatives. No nonzero expansion at remote real
colors is claimed. The comparison needed for a selected next
source still retains the conditional action, selected
halfweight, affine marginal, and correlated reference action.
The scalar inequality (21) alone does not decide that comparison.

## 5. A sharper real-primitive bound

The preceding proof remains valid as written. The following
elementary refinement improves only (5). Set \(d=4/25\).
Because \(-J\) is increasing before \(1/6\), (1) gives
\(-J(1/2-x_+)<-J(d)\). For \(0\le s\le d\),
\[
 \sin(\pi s)\ge\pi s(1-\pi^2s^2/6),\qquad
 -\log(1-\pi^2s^2/6)
       \le\frac{\pi^2s^2}{6(1-\pi^2d^2/6)}.
                                                                    \tag{22}
\]
Integrating these inequalities yields
\[
 -J(d)\le d\{1-\log(2\pi d)\}
             +\frac{\pi^2d^3}{18(1-\pi^2d^2/6)}.
                                                                    \tag{23}
\]
Use \(\pi>157/50\), \(\pi^2<10\), and
\[
 \log(2\pi d)>\log(628/625)>
                          \frac{(628/625)-1}{628/625}
                          =\frac3{628}.
                                                                    \tag{24}
\]
The last logarithm inequality follows by integrating \(1/t>1/u\)
from \(1\) to \(u>1\).
At \(d=4/25\), (23)--(24) give
\[
 -J(d)<\frac{25}{157}+\frac{64}{26925}
      <\frac{25}{157}+\frac1{420}
       =\frac{10657}{65940}<\frac{97}{600}.
                                                                    \tag{25}
\]
The middle comparison uses \(64\cdot420<26925\);
the last has positive cross-product difference \(1980\).

Replacing \(1/6\) in (6) and (21) by \(97/600=1/6-1/200\)
therefore proves
\[
 \boxed{\quad
 M_{\rm half}
       <\frac{203}{200}-\frac{1303}{7680000}
       <\frac{203}{200}.
 \quad}                                                         \tag{26}
\]
The strict \(203/200\) ceiling has the same fixed local
complex-neighborhood and all-real upper-bound consequences
described after (21). It still makes no selected affine
comparison or extension to the macroscopic incoming arc.

