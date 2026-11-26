# Simultaneous zero-frequency contour transport for the contracted pair

Research deduction, 7 November 2026. The four real index contours
can be moved to their original critical heights by a single
homotopy. Its joining currents have a common height parameter,
so the physical-face gap and the critical-height-face gap control
them by convexity. The complete lattice correction is retained as
an exact separate term; it is not estimated by this argument.

## 1. Retain the exact lattice correction

Let \(F_N(z_1,z_2,z_3,z_4;x,y)\) be the whole holomorphic
row interpolant of
[the contracted source](research_mixed_contracted_pair_rectangle.md),
including its original outside scalar. Its index order is
\((s,t,p,q)\), and its phase is \(\mathcal F\) of that theorem.
Use half-grid cuts \(a_{j,N},b_{j,N}\) enclosing exactly the
lattice points of the original central interval in coordinate \(j\).
Their differences from the fixed cuts of
\(C=[1/4,9/20]^2\times[1/5,21/50]^2\) are \(O(N^{-1})\).
Write \(C_N=\prod_j[a_{j,N},b_{j,N}]\).

For all sufficiently large \(N\), this entire central box lies
strictly inside the three physical support inequalities. The exact
interpolant is holomorphic on a neighborhood of its product of
original height rectangles. These facts follow from the strict
strip margins in the contracted source theorem; no triangular
support is extended across a nonzero row.

In coordinate \(j\), retain its original lower and upper heights
\(h_{j,-}<0<h_{j,+}\). Define four linear operators, leaving
all other variables and parameters unchanged:
\[
\begin{split}
 I_jF&=N\int_{a_{j,N}}^{b_{j,N}}F(z_j=u)\,du,\\
 A_j^-F&=N\int_{a_{j,N}}^{b_{j,N}}
 F(z_j=u+ih_{j,-})
 \frac{e^{-2\pi iN(u+ih_{j,-})}}{1-e^{-2\pi iN(u+ih_{j,-})}}\,du,\\
 A_j^+F&=N\int_{a_{j,N}}^{b_{j,N}}
 F(z_j=u+ih_{j,+})
 \frac{e^{2\pi iN(u+ih_{j,+})}}{1-e^{2\pi iN(u+ih_{j,+})}}\,du,\\
 V_jF&=iN\int_{h_{j,-}}^{h_{j,+}}w_{N,0}(v)
       [F(z_j=b_{j,N}+iv)-F(z_j=a_{j,N}+iv)]\,dv,\\
 w_{N,0}(v)&=\frac1{1+e^{2\pi Nv}}-\boldsymbol1_{\{v<0\}}.
\end{split}
 \tag{1}
\]
The value assigned at \(v=0\) is immaterial. The derivation of
[vertical regrouping](research_exact_vertical_current_regrouping.md)
applies with the zero-frequency line placed at height zero, and gives
the exact identity
\[
 \sum_{a_{j,N}<k/N<b_{j,N}}F(z_j=k/N)
                         =(I_j+A_j^-+A_j^++V_j)F.
 \tag{2}
\]
In particular \(|w_{N,0}(v)|\le e^{-2\pi N|v|}\).
The upper and lower horizontal factors have their full original
denominators. No Fourier mode or vertical-side difference is removed.

Operators in distinct variables commute. Let
\(O_{j,0}=I_j\), \(O_{j,-}=A_j^-\),
\(O_{j,+}=A_j^+\), \(O_{j,v}=V_j\), and define
\[
 \mathcal A_N=
 \sum_{\substack{\sigma\in\{0,-,+,v\}^4\\\sigma\ne(0,0,0,0)}}
             O_{1,\sigma_1}O_{2,\sigma_2}
                         O_{3,\sigma_3}O_{4,\sigma_4}F_N.
 \tag{3}
\]
This is the sum of all 255 nonzero lattice-correction terms.
Splitting the left and right parts of each \(V_j\) recovers
the corresponding 624 nonmain tensor currents. Keeping their
differences is an exact grouping before modulus. The central
finite lattice sum is exactly
\[
                   N^4\int_{C_N}F_N(u;x,y)\,du+\mathcal A_N.
 \tag{4}
\]

## 2. One common height parameter for the zero-frequency integral

Let
\[
 h=(\Im z_3,\Im z_3,\Im z_4,\Im z_4)
 \tag{5}
\]
be the original fixed critical height vector. Set
\[
 \mathcal M_N=N^4\int_{C_N}F_N(u+ih;x,y)\,du.
\]
For coordinate \(j\), write \(u_{\widehat j}\) for the other
three real coordinates, and \(C_{N,\widehat j}\) for their
box. Let \(u^{j,+}\) and \(u^{j,-}\) be the real vectors
obtained by inserting \(b_{j,N}\) and \(a_{j,N}\), respectively,
in their \(j\)-th coordinate. Define the complete oriented joining term
\[
\begin{split}
 \mathcal J_N=iN^4\sum_{j=1}^4h_j\int_0^1
 \int_{C_{N,\widehat j}}
 \big[&F_N(u^{j,+}+i\lambda h;x,y)\\
       -&F_N(u^{j,-}+i\lambda h;x,y)\big]
                     \,du_{\widehat j}\,d\lambda.
\end{split}
 \tag{6}
\]
Here (6) means simply that all four complex coordinates have the
same height multiplier \(\lambda\), with the \(j\)-th real
coordinate fixed at its indicated face. The external parameters
\(x,y\) are unchanged throughout.

The exact transport identity is
\[
                N^4\int_{C_N}F_N(u;x,y)\,du
                           =\mathcal M_N-\mathcal J_N.
 \tag{7}
\]
To prove it, differentiate
\(N^4\int_{C_N}F_N(u+i\lambda h;x,y)\,du\)
with respect to \(\lambda\). Holomorphy gives
\(i\sum_jh_j\partial_{u_j}F_N\); integration in each
\(u_j\) gives precisely the face difference in (6).
Integrating from zero to one proves (7), including its sign.
Equivalently this is Stokes' theorem for the closed holomorphic
four-form under the simultaneous translation homotopy.

If \(\mathcal P_N\) denotes the remaining physical lattice
rows of (2) in the contracted source theorem, then the complete
original kernel is exactly
\[
                \mathcal K_{34,N}=\mathcal P_N+
                           \mathcal M_N-\mathcal J_N+\mathcal A_N.
 \tag{8}
\]
Every scalar, parity convention and physical-support zero is retained.

## 3. A physical-face gap also pays the simultaneous joins

Initially set \(x=y=x_0\), and let \(M=\Re\mathcal F_*\).
Suppose the eight physical central faces have a common gap
\[
                       \sup_{u\in\partial C}E(u)\le M-\delta_0,
                       \qquad\delta_0>0.
 \tag{9}
\]
This is part of the still-unevaluated
[nine-face physical-tail comparison](research_mixed_contracted_pair_nine_face_tail.md).
The full tail includes its ninth face and far-region bound, but
neither is needed just for (9).

Let \(d>0\) be the Euclidean distance from the real part of
the original critical point to \(\partial C\). Whole-rectangle
accretivity gives on every critical-height face
\[
                   \Re\mathcal F(u+ih)\le M-\delta_1,
                   \qquad\delta_1=\mu d^2/2>0.
 \tag{10}
\]
For fixed real \(u\), holomorphy and the same Hessian bound give
\[
 \frac{d^2}{d\lambda^2}\Re\mathcal F(u+i\lambda h)
              =-h^T\Re\mathcal F''(u+i\lambda h)h\ge0.
 \tag{11}
\]
Thus convexity, (9), and (10) imply
\[
 \Re\mathcal F(u+i\lambda h)
 \le(1-\lambda)E(u)+\lambda\Re\mathcal F(u+ih)
 \le M-\min(\delta_0,\delta_1)
 \tag{12}
\]
for every \(u\in\partial C\) and \(0\le\lambda\le1\).
All joining paths in (6) use exactly this common multiplier;
independently chosen intermediate heights are not substituted.

The uniform original symbol bounds then make \(\mathcal J_N\)
exponentially smaller than \(e^{NM}\), up to a polynomial.
Half-grid shifts and a sufficiently small fixed neighborhood in
\(x,y\) use a smaller positive gap, by continuity and the strict
strip margins. The same conclusion holds for fixed derivatives,
by the holomorphic bounds on a slightly larger neighborhood.

Consequently a successful nine-face comparison would control both
the entire physical tail \(\mathcal P_N\) and all the joining
terms \(\mathcal J_N\) in (8). The nonzero local term
\(\mathcal M_N\) has the explicit original coefficient already
proved in the contracted rectangle theorem. No estimate for
\(\mathcal A_N\) follows from (9)--(12): it includes the full
horizontal aliases and the regrouped vertical lattice corrections.
In particular (8) does not yet imply a whole-kernel asymptotic.

## 4. Original gradient strips pay every vertical lattice correction

There is an additional uniform analytic fact on the entire original
product rectangle, at \(x=y=x_0\):
\[
                     |\Im\mathcal F_j|<2\pi,
                         \qquad j\in\{s,t,p,q\}.
 \tag{13}
\]
To fix its lifts as well as its inequalities, recall the exact
identity \(g'(z)=\operatorname{Log}(1-e^{-2\pi iz})\)
on the original strip. Every argument of \(g'\) below has real
part in \([.2,.9]\) and imaginary part at most \(.03\).
The complex number inside its logarithm has positive real part because
\[
 e^{.06\pi}<\frac{49}{40},\qquad
 \cos(\pi/5)=\frac{1+\sqrt5}{4}<\frac{13}{16},
 \qquad \frac{49}{40}\frac{13}{16}=\frac{637}{640}<1.
 \tag{14}
\]
The exponential comparison follows from \(.06\pi<1/5\) and
\[
 e^{1/5}\le1+\frac15+
       \frac{(1/5)^2}{2(1-(1/5)/3)}
       =\frac{171}{140}<\frac{49}{40}.
\]
Thus the original imaginary parts \(\Im g'(z)\) lie in
\((-\pi/2,\pi/2)\). They are positive for an own index
\(t,p,q\), and nonpositive for \(s+t\), whose real part
is at least \(1/2\). These statements concern the argument
of \(1-e^{-2\pi iz}\), not the argument of the logarithm itself.
Continuation from the real strip supplies the exact original lift.

For either external incidence, \(Ke^{-2\pi is}\) or
\(Ke^{-2\pi iq}\) lies strictly in the lower half-plane and
has modulus less than \(.7\). Therefore
\[
 \Im\ell_{s,s}(x_0)
    =2\pi\Re x_0-\arg(1-Ke^{-2\pi is})\in(-\pi/2,\pi/2),
 \tag{15}
\]
and similarly for \(q\). Differentiate the literal phase:
\[
\begin{split}
 \mathcal F_s&=g'(s+t)+\ell_{s,s}(x_0),\\
 \mathcal F_t&=g'(s+t)+g'(t+p)-2g'(t)+2\pi ip,\\
 \mathcal F_p&=g'(t+p)+g'(p+q)-3g'(p)+2\pi it,\\
 \mathcal F_q&=g'(p+q)-g'(q)+\ell_{q,q}(x_0).
\end{split}
 \tag{16}
\]
The preceding signs and original real-coordinate ranges give
\[
\begin{array}{c|c}
 j&\Im\mathcal F_j/\pi\\\hline
 s&(-1,1/2)\\
 t&(-8/5,67/50)\\
 p&(-2,19/10)\\
 q&(-3/2,1).
\end{array}
 \tag{17}
\]
For example the lower \(p\) bound is strictly
\(-1-3/2+1/2=-2\): both summed arguments have imaginary
logarithm greater than \(-\pi/2\), each own logarithm is
less than \(\pi/2\), and \(\Re t\ge1/4\).
This proves (13). Compactness gives a uniform strict margin,
which survives small half-grid and endpoint perturbations.

For real \(u\in C\) and an allowed height vector \(v\), define
\[
                 W(u,v)=\Re\mathcal F(u+iv)-2\pi\sum_j|v_j|.
 \tag{18}
\]
Integrating (13) from height zero gives
\(W(u,v)\le E(u)\). Equivalently, in each fixed-sign height
coordinate \(W\) strictly decreases as its absolute height
increases away from zero. All intermediate points stay in the
same original rectangle.

Every term of (3) which contains a \(V_j\) has at least one
real coordinate on a central face. Its vertical weights have
modulus at most \(e^{-2\pi N|v_j|}\). A horizontal alias
weight has modulus at most
\[
 \frac{e^{-2\pi N|h_{j,\pm}|}}
                  {1-e^{-2\pi N|h_{j,\pm}|}},
 \tag{19}
\]
whose denominator is uniformly bounded away from zero for all
sufficiently large \(N\). Thus every such grouped term, after
retaining and then bounding its side differences, has rate at most
the physical-face maximum in (9). The uniform row symbols and
the factors \(N\) cost only a polynomial. Consequently (9)
also pays all vertical lattice corrections in \(\mathcal A_N\).

## 5. Eight purely horizontal alias comparisons remain

Terms in (3) with no \(V_j\) have a fixed height vector
\[
 v_j\in\{0,h_{j,-},h_{j,+}\},\qquad v\ne0.
\]
There are \(3^4-1=80\) such products. For any one of them,
retain one nonzero component \(v_j=h_{j,\pm}\) and reset
all other heights to zero. The monotonicity of (18) gives
\[
 W(u,v)\le W(u,h_{j,\pm}e_j).
 \tag{20}
\]
Hence the largest containing rate of all 80 products is exactly
the largest of the eight single-coordinate maxima
\[
 B_{j,\pm}=\max_{u\in C}
    \{\Re\mathcal F(u+ih_{j,\pm}e_j)-2\pi|h_{j,\pm}|\}.
 \tag{21}
\]
The reverse inequality is immediate because these eight height
vectors are among the original 80. There is no change to their
original fixed heights and no choice of a new saddle.

Each function in (21) is strictly concave in the four real
coordinates, by the whole-rectangle Hessian theorem. A tangent at
any fixed point of \(C\) is therefore a rigorous global upper
bound on it, with all four signed support terms retained. The
finite denominators in (19), including products of them, have
already been accounted for as bounded factors; no exponential
normalization is omitted.

If the nine physical-face comparisons in the preceding note and
these eight alias comparisons are all strictly below \(M\),
then every nonmain term in (8) has a common positive exponential
gap: the far physical region uses its proved \(1/200\) gap,
the joins also use the positive critical-height-face gap (10),
and all remaining pieces use the strict face and alias margins.
This would prove the full original paired kernel asymptotic with
the nonzero coefficient of \(\mathcal M_N\), on a fixed smaller
endpoint neighborhood and with all fixed derivatives and both
parities. The seventeen scalar comparisons have not been evaluated
here. The result is a finite criterion for this paired kernel;
it does not assert a whole cap-message remainder estimate or a
cofinite-filling theorem.
