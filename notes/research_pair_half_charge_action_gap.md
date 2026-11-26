# The pair color lies beyond the half-charge observation contour

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The actual angle at either vertex of a positive complete-ended
internal pair lies strictly below and to the right of the
corresponding half-charge leaf saddle. Its half-charge action is
strictly larger. Both statements follow from the original logarithmic
periods and elementary bounds for a single analytic derivative.
They do not assume a nonzero coefficient for the filled pair.

This supplies the geometric comparison needed to evaluate the
[proved half-charge Cauchy observation](research_complete_source_pick_observation.md)
at an actual pair color. The exact Cauchy residue and interpolation
remainder must still be kept when making that source substitution.

## 1. Original periods and the half-charge reference

Fix integer powers \(n,p\ge3\), with unit charges at the two
selected vertices and one complete outside endpoint at each.
Write their positive angles as \(t=a-iH\) and \(u\). The proved
[pair angle bound](research_internal_pair_angle_bound.md),
[complete-edge height bound](research_internal_pair_complete_edge_gap.md),
and [cosine maximum principle](research_positive_path_real_wire_order.md)
give
\[
 0<a<\frac{\pi}{2},\qquad 0<H<\frac{107}{100},\qquad
                  |\cos(u/2)|<1.
 \tag{1}
\]
The two original returns at \(t\) are
\[
 r_0(t)=\operatorname{asinh}\tan(t/2),\qquad
 r_1(t,u)=\operatorname{asinh}\{\tan(t/2)\cos(u/2)\}=k+ig,
 \quad k>0,\quad |g|<\pi/2.
 \tag{2}
\]
Their logarithmic filling equation is
\[
                    nt+2i\{r_0(t)+r_1(t,u)\}=2\pi.
 \tag{3}
\]
All branches are the selected ones continued from completeness.

Put
\[
 f_n(z)=nz+2ir_0(z),\qquad
 S_n(z)=\Psi(z)+\frac{inz^2}{4\pi}-\frac{iz}{2},
 \quad \Psi(z)=\psi(z,0).
 \tag{4}
\]
The original complete constant is retained in \(\Psi\). In particular
\[
 S_n'(z)=\frac{i}{2\pi}\{f_n(z)-\pi\},\qquad
                       f_n'(z)=n+i\sec(z/2).
 \tag{5}
\]
Let \(t_0=a_0-iH_0\) be the half-charge saddle
\[
 f_n(t_0)=\pi,\qquad
       0<a_0<\pi/3,\quad 0<H_0<2/5,\qquad
                   M_n=\Re S_n(t_0).
 \tag{6}
\]
Its existence, uniqueness, branches, and actual observation
coefficient are proved in Sections 5–6 of the linked half-charge
note. No geometric or source coefficient is selected by an
exponentiated equation here.

## 2. Two elementary cones

**Lemma 1.** The original internal return in (2) satisfies
\[
                       0<k<\pi/2+g .
 \tag{7}
\]

*Proof.* On (1),
\[
 |\tan(t/2)|^2
   =\frac{\cosh H-\cos a}{\cosh H+\cos a}<1.
\]
Together with \(|\cos(u/2)|<1\), this gives
\[
                     \sinh^2 k+\sin^2g
                              =|\sinh r_1|^2<1.
 \tag{8}
\]
If \(g\le0\), put \(v=\pi/2+g\in(0,\pi/2]\). Then
\(\sinh k<\sin v\), so
\(k<\operatorname{asinh}(\sin v)<v\).
The last strict inequality follows from
\(\operatorname{asinh}x<x\) for \(x>0\) and
\(\sin v\le v\). If \(g>0\), use
\(k<\operatorname{asinh}1<1<\pi/2+g\).
This proves (7). \(\square\)

**Lemma 2.** Throughout the rectangle
\[
          0<a<\pi/2,\qquad 0<H<107/100,\qquad z=a-iH,
\]
one has
\[
 \frac67<\Re\sec(z/2)<\frac{10}{7},\qquad
                  0<-\Im\sec(z/2)<\frac12.
 \tag{9}
\]
Consequently, writing \(f_n'(z)=A(z)+iB(z)\),
\[
             n<A(z)<n+\frac12,\qquad
                         \frac67<B(z)<\frac{10}{7}.
 \tag{10}
\]

*Proof.* Set \(c=\cos(a/2)\) and \(v=\sinh(H/2)\). Then
\[
 \Re\sec(z/2)=\frac{c\sqrt{1+v^2}}{c^2+v^2},\qquad
 -\Im\sec(z/2)=\frac{\sin(a/2)v}{c^2+v^2}.
 \tag{11}
\]
Here \(c>1/\sqrt2\). A geometric majorant for the positive
cosh series gives
\[
 \cosh(H/2)<\cosh(11/20)
 \le 1+\frac{(11/20)^2}{2\{1-(11/20)^2/12\}}
       =\frac{5405}{4679}<\frac76.
 \tag{12}
\]
The majorant bounds each ratio after the quadratic term by
\((11/20)^2/12\). Hence \(v^2<13/36<1/2<c^2\).
The first expression in (11), at fixed \(v\), decreases with
\(c\) because its derivative has the sign of \(v^2-c^2\).
It is therefore at least \(1/\sqrt{1+v^2}>6/7\).
It is at most \(1/c<\sqrt2<10/7\): after multiplication by
the positive denominators this uses
\(c^2(\sqrt{1+v^2}-1)\le v^2\).
Finally \(c^2+v^2\ge2cv\), so the second expression in (11)
is at most \(\tan(a/2)/2<1/2\).
All its factors are positive. This proves (9) and (10).
\(\square\)

## 3. Position and a quantitative action gap

**Theorem 3.** For the actual pair angle \(t\), put
\[
                    t-t_0=d-ih .
\]
Then
\[
                  d>0,\qquad h>0,
 \tag{13}
\]
and the half-charge actions obey
\[
 \boxed{\quad
 \Re S_n(t)-M_n
       >\frac{d^2}{98\pi}+\frac{3h^2}{14\pi}>0 .
 \quad}
 \tag{14}
\]
The corresponding statement holds at the other vertex with
power \(p\).

*Proof.* By the exact logarithmic equation (3),
\[
 f_n(t)-f_n(t_0)
       =\pi+2g-2ik=R-iK,\qquad
          R=2(\pi/2+g),\quad K=2k.
 \tag{15}
\]
Lemma 1 gives \(0<K<R\).
The straight segment from \(t_0\) to \(t\) lies in the
rectangle of Lemma 2. Put
\[
 \overline A+i\overline B
             =\int_0^1 f_n'(t_0+s(t-t_0))\,ds.
\]
The bar here means an average, not complex conjugation.
The fundamental theorem of calculus gives
\[
 d=\frac{\overline A R-\overline B K}
          {\overline A^2+\overline B^2}>0,\qquad
 h=\frac{\overline B R+\overline A K}
          {\overline A^2+\overline B^2}>0 .
 \tag{16}
\]
For the first sign use \(\overline A>n\ge3>10/7>\overline B\)
and \(K<R\). Moreover
\[
       \frac hd>\frac{\overline B}{\overline A}
                         >\frac{6}{7(n+1/2)}.
 \tag{17}
\]

Since \(S_n'(t_0)=0\), integrating (5) twice gives the exact
identity
\[
 S_n(t)-S_n(t_0)=\frac{i(d-ih)^2}{2\pi}
       \int_0^1(1-s)f_n'(t_0+s(t-t_0))\,ds.
 \tag{18}
\]
Write the last integral as \(\widetilde A+i\widetilde B\).
From (10),
\(\widetilde A>n/2\) and \(3/7<\widetilde B<5/7\).
Taking real parts of (18) and using (17) therefore gives
\[
 \begin{split}
 \Re\{S_n(t)-S_n(t_0)\}
 &=\frac{2\widetilde A dh+
               \widetilde B(h^2-d^2)}{2\pi}\\
 &>\frac{n-5/2}{14\pi(n+1/2)}\,d^2
                       +\frac{3}{14\pi}\,h^2\\
 &\ge\frac{d^2}{98\pi}+\frac{3h^2}{14\pi},
 \end{split}
 \tag{19}
\]
where the final comparison uses \(n\ge3\).
This proves the theorem. \(\square\)

For each fixed pair the right side of (14) is a fixed
positive number. By continuity, a smaller positive gap
persists on a fixed complex neighborhood of its selected
angle. No uniform positive gap as the powers tend to infinity
is asserted.

The position statement is also exactly the one needed by the
Cauchy observation contour. Its angular rectangle has real
ends tending to \(\pm\pi/2\) and imaginary heights \(\pm H_0\).
The two preimages \(t,-t\) of the pair color \(-2\cos t\)
lie strictly outside that rectangle, because \(H>H_0\).
They remain separated from it on a fixed neighborhood.
There are no further preimages in that angular period.
Thus an exact residue formula for evaluation at this color
uses its exterior case, not the case where the evaluation
pole is enclosed and cancels the direct term.

These statements compare a specified original pair angle with
a specified original-source observation action. They do not
identify the coefficient of the full signed pair contraction.
In particular the complementary-time observations, the shared
wire, and all ordinary boundary normals must still be retained
in that contraction.

## 4. The actual local normal defect at even levels

Here is the source consequence, using the exact residue formula
and exterior observation packet proved independently in
[the observation note, equation (34) and Corollary 4](research_complete_source_pick_observation.md#complex-colors-and-the-exact-normal-defect).
At \(N=2m\), put \(Q(w)=2T_m(w/2)\), let
\[
 h_{n,N}(w)
  =e^{inN\arccos(-w/2)^2/(4\pi)}\mathcal L_N(w),
\]
and let \(\mathcal I_{n,N}\) be its ordinary value interpolant of
degree less than \(m\) at the distinct physical roots. The
holomorphic normal defect is
\[
 \mathscr D_{n,N}(w)
       =\frac{h_{n,N}(w)-\mathcal I_{n,N}(w)}{Q(w)}.
 \tag{20}
\]
It retains the actual first normals through
\(h'_{n,N}(c_a)-\mathcal I'_{n,N}(c_a)
   =Q'(c_a)\mathscr D_{n,N}(c_a)\).
The original crossing scalar multiplies both sides when restored.

For every fixed pair in Theorem 3, there are a fixed complex
neighborhood of its angle \(t\) and \(\delta>0\) such that
\[
 \begin{split}
 \mathscr D_{n,N}(-2\cos z)
 &=\frac{h_{n,N}(-2\cos z)}{Q(-2\cos z)}
                  \left(1+O(N^{-1/2}e^{-\delta N})\right)\\
 &=(-1)^m N^{-3/2}a_e(z,0)e^{NS_n(z)}
                  \left(1+O(N^{-1})\right)\ne0
 \end{split}
 \tag{21}
\]
for all large even levels. All fixed ordinary complex-color
derivatives have the corresponding differentiated holomorphic
expansions on smaller neighborhoods.

Indeed Theorem 3 places the color outside the exact observation
rectangle, so the exterior residue formula applies. That formula
gives \(\mathcal I_{n,N}/Q=O(N^{-2}e^{NM_n})\), whereas the
complete-edge packet and the exact cosine denominator give the
direct term \(N^{-3/2}a_e e^{NS_n}\), with the parity scalar in
(21). The strict action gap (14), reduced slightly on the
neighborhood, gives the first relative error in (21).
This proves the application; it was not an input to the
geometric argument in Sections 1–3.

Thus a nonzero local source is proved, including its ordinary
normal directions. The remaining whole signed pair contraction
still requires the rest of its contour to be controlled.

