# A full-source contour criterion for the prepared three-four cap

Research deduction, 7 November 2026. The original prepared-cap phase
has a strict imaginary-gradient bound on its whole regular rectangle.
Consequently its four-index lattice corrections reduce to eight
single-height comparisons, while its simultaneous joining currents
are paid by the physical faces. Together with the proved physical-tail
reduction, this gives a sufficient criterion for the complete prepared
cap, with its own action and nonzero amplitude. The required critical
point and strict comparisons are hypotheses, not evaluated conclusions.

## 1. Original source, rectangle and fixed calibration

Use the exact function and row interpolation of
[the prepared-cap source theorem](research_mixed_prepared_three_four_cap_source.md):
\[
 G_{34,N}(y,w)=v_N(w)^T A_{3,N}A_{4,N}h_N(y).
 \tag{1}
\]
The base parameters are \((y,w)=(x_0,-2)\), with
\[
 K=e^{2\pi ix_0}=(1+2a-4a^2)^{-1},
 \tag{2}
\]
where \(a\) is the original isolated quartic root, with the
original branch identification in
[the power-three reference packet](research_three_vertex_mixed_reference_packet.md),
equation (2). No root, logarithmic lift, or additive action constant
is selected anew.

In the source index order \(z=(s,t,p,q)\), put
\[
\begin{split}
 C&=[27/100,49/100]\times[11/50,1/2]\times[1/5,21/50]^2,\\
 h_-&=(-11/200,-9/125,-51/500,-51/500),\\
 h_+&=(1/25,21/1000,3/200,3/200),\\
 \mathscr R&=\{u+iv:u\in C,\ h_{j,-}\le v_j\le h_{j,+}\}.
\end{split}
 \tag{3}
\]
This is the [typed-height prepared rectangle](research_mixed_prepared_cap_typed_height_rectangle.md),
with heights \([-.055,.04]\), \([-.072,.021]\), and
\([-.102,.015]\) for each of the last two coordinates.
Its three sum-real intervals are \([.49,.99]\),
\([.42,.92]\), and \([.4,.84]\). The central box is
strictly inside all three physical supports.

Write \(F=\mathcal F_{\mathrm{cap}}\). Explicitly, on the
original branches,
\[
\begin{split}
 F(z;y,w)={}&S(s,w)-\frac{\pi i}{2}(s-s^2)
 +g(s+t)+g(t+p)+g(p+q)\\
 &-2g(t)-3g(p)-g(q)+2\pi itp+\ell_q(y),\\
 \ell_q(y)&=2\pi iqy-
 \frac{\operatorname{Li}_2(e^{2\pi iy-2\pi iq})-
       \operatorname{Li}_2(e^{2\pi iy})}{2\pi i}-\pi iy.
\end{split}
 \tag{4}
\]
The source theorem and its typed-height extension prove on a
neighborhood of \(\mathscr R\) the original full-row expansion
\[
 f_N(z;y,w)=\kappa^3N^{-3}b_{\mathrm{cap}}(z;y,w)
          e^{NF(z;y,w)}(1+O(N^{-1})),
 \qquad b_{\mathrm{cap}}\ne0,
 \tag{5}
\]
and a uniform Hessian bound
\(-\Re F''\succeq\mu I_4\), \(\mu>0\), for nearby
parameters. The symbol in (5) is exactly equation (18) of that
theorem, including the endpoint carrier and outgoing square roots.
The endpoint coefficient in this row is its whole specified
holomorphic finite sum; no private Newton remainder is omitted.

At the base parameters, the zero-height real phase equals the
coherent physical rate
\[
 E(u)=\Re F(u;x_0,-2)=E_\lambda(u).
 \tag{6}
\]
The [prepared physical-tail theorem](research_mixed_prepared_cap_physical_tail_reduction.md)
proves the upper rate
\[
 P_*:=\max\left\{\frac{146}{75},
                      \max_{u\in\partial C}E(u)\right\}
 \tag{7}
\]
for the entire complementary physical sum. Its literal true-index
endpoint estimates, all three support faces, both parities and
fixed ordinary jets are included. Equation (7) is specific to the
prepared source; the completed paired kernel's action and numerical
margins are not substituted.

## 2. The prepared gradient bound holds before outer stationarity

**Lemma 1.** On the whole closed rectangle \(\mathscr R\), at
\((y,w)=(x_0,-2)\),
\[
                  |\Im F_j|<2\pi,\qquad j=s,t,p,q.
 \tag{8}
\]
There is a common strict margin, which persists on a neighborhood
of the rectangle and a sufficiently small fixed parameter neighborhood.

*Proof.* Use the original endpoint branch \(u_c(s)\). The endpoint
cap theorem gives throughout its closed \(s\)-rectangle
\[
       0<\Re u_c(s)<\Re s<1/2,\qquad \Im u_c(s)>0.
\]
The proof of Section 2 of
[the original prepared critical curve](research_mixed_prepared_three_four_cap_critical_curve.md)
uses the elementary inequality
\[
 \min(0,\pi(1-2x))\le\Arg(1-r e^{-2\pi ix})
               \le\max(0,\pi(1-2x)),\qquad r>0,
 \tag{9}
\]
for \(0<x<1\). The bounds are strict away from the zero
argument at \(x=1/2\). Substituting \(u_c(s)\) into the
five-variable phase gives exactly (4); its endpoint derivative is
already zero. The four remaining derivatives are therefore the
four displayed outer derivatives in equation (3) of that note.

For the \(s\) derivative, the original calibration gives
\[
 F_s=\Log(1-ZT)-\Log(1-Z/U)+2\pi i u_c(s),
 \quad (Z,T,U)=(e^{-2\pi is},e^{-2\pi it},e^{-2\pi iu_c(s)}).
\]
Here the first logarithm has imaginary part in \((-\pi,\pi)\),
the second in \((0,\pi)\), and \(2\pi\Re u_c(s)\in(0,\pi)\).
Hence \(-2\pi<\Im F_s<2\pi\).
The other three bounds are precisely the elementary sums of
arguments in equations (12)--(13) of the critical-curve proof:
\[
 \begin{array}{c|c}
 j&\Im F_j/\pi\\\hline
 t&(-29/25,51/50)\\
 p&(-9/5,34/25)\\
 q&(-41/25,3/5).
 \end{array}
 \tag{10}
\]
They use only the real coordinate intervals in (3),
\(0<\Re x_0<1/5\), and the original logarithm branches.
Neither the rational closing equation nor any of the four outer
stationary equations is used in these inequalities. Thus these
are whole-rectangle bounds, not just bounds at an admitted root.
Continuity on the compact rectangle supplies the uniform margin
and its stated extensions. \(\square\)

For \(u\in C\) and an allowed height vector \(v\), define
\[
                  W(u,v)=\Re F(u+iv;x_0,-2)-2\pi\sum_j|v_j|.
 \tag{11}
\]
If a height coordinate has sign \(\sigma\in\{-1,1\}\),
its derivative with respect to its absolute value is
\(-\sigma\Im F_j-2\pi<0\). Consequently resetting any
height coordinate to zero increases \(W\). In particular,
\[
 W(u,v)\le E(u),\qquad
 W(u,v)\le W(u,h_{j,\pm}e_j)
 \quad\hbox{if }v_j=h_{j,\pm}.
 \tag{12}
\]
All intermediate points remain inside the same rectangle.

## 3. Exact lattice decomposition and common-height joins

Choose half-grid cuts \(a_{j,N},b_{j,N}\) enclosing exactly the
physical nodes in the corresponding fixed central interval. Write
\(C_N=\prod_j[a_{j,N},b_{j,N}]\). These cuts differ from
those of \(C\) by \(O(N^{-1})\). For large \(N\),
the source interpolation is holomorphic on a neighborhood of the
whole corresponding product of height rectangles, and the three
support inequalities remain strict.

For one coordinate, leaving the other arguments unchanged, define
\[
\begin{split}
 I_j f&=N\int_{a_{j,N}}^{b_{j,N}}f(u)\,du,\\
 A_j^- f&=N\int_{a_{j,N}}^{b_{j,N}}f(u+ih_{j,-})
  \frac{e^{-2\pi iN(u+ih_{j,-})}}
       {1-e^{-2\pi iN(u+ih_{j,-})}}\,du,\\
 A_j^+ f&=N\int_{a_{j,N}}^{b_{j,N}}f(u+ih_{j,+})
  \frac{e^{2\pi iN(u+ih_{j,+})}}
       {1-e^{2\pi iN(u+ih_{j,+})}}\,du,\\
 V_j f&=iN\int_{h_{j,-}}^{h_{j,+}}w_{N,0}(v)
       [f(b_{j,N}+iv)-f(a_{j,N}+iv)]\,dv,\\
 w_{N,0}(v)&=\frac1{1+e^{2\pi Nv}}-\boldsymbol1_{\{v<0\}}.
\end{split}
 \tag{13}
\]
The [exact vertical regrouping](research_exact_vertical_current_regrouping.md),
with zero-frequency height zero, gives
\[
 \sum_{a_{j,N}<k/N<b_{j,N}}f(k/N)
                    =(I_j+A_j^-+A_j^++V_j)f.
 \tag{14}
\]
This also follows directly from its lower-base residue formula
by moving the constant lower integral to height zero. Thus its
use here does not require a negative saddle height. The vertical
subtraction is made before taking a modulus. The bounds are
\[
 |w_{N,0}(v)|\le e^{-2\pi N|v|},\qquad
 \left|\frac{e^{\pm2\pi iN(u+ih_{j,\pm})}}
 {1-e^{\pm2\pi iN(u+ih_{j,\pm})}}\right|
 \le\frac{e^{-2\pi N|h_{j,\pm}|}}
                {1-e^{-2\pi N|h_{j,\pm}|}}.
 \tag{15}
\]

Tensor (14) in all four variables. Let \(\mathcal A_N\) be
the sum of its 255 products other than \(I_1I_2I_3I_4 f_N\).
Splitting the two sides of each \(V_j\) gives the same
624 nonmain tensor currents. No term, side difference or finite
alias denominator is discarded.

Suppose an original critical point \(z_*\) lies strictly inside
\(\mathscr R\). Put \(h_* =\Im z_*\),
\(M=\Re F(z_*;x_0,-2)\), and
\[
 \mathcal M_N=N^4\int_{C_N} f_N(u+ih_*;y,w)\,du.
\]
For a face vector \(u^{j,+}\) or \(u^{j,-}\), insert
\(b_{j,N}\) or \(a_{j,N}\) in its \(j\)-th real coordinate.
The complete common-height joining current is
\[
\begin{split}
 \mathcal J_N=iN^4\sum_j h_{*,j}\int_0^1\int_{C_{N,\widehat j}}
 [f_N(u^{j,+}+i\theta h_*;y,w)
       -f_N(u^{j,-}+i\theta h_*;y,w)]\,du_{\widehat j}\,d\theta.
\end{split}
 \tag{16}
\]
Differentiating the four-dimensional integral under simultaneous
height translation proves, with the displayed orientations,
\[
 G_{34,N}=\mathcal P_N+\mathcal M_N-\mathcal J_N+\mathcal A_N,
 \tag{17}
\]
where \(\mathcal P_N\) is the original complementary physical
sum. Formula (17) retains its scalar \(\kappa^3\), every
physical support zero and both level parities.

If \(\max_{\partial C}E<M\), put
\(\delta_f=M-\max_{\partial C}E>0\) and
\(d=\operatorname{dist}(\Re z_*,\partial C)>0\).
Strict real concavity at the critical height gives
\[
       \Re F(u+ih_*;x_0,-2)\le M-\mu d^2/2,
                         \qquad u\in\partial C.
 \tag{18}
\]
For the *same* real face point, holomorphy and the negative real
Hessian give
\[
 \frac{d^2}{d\theta^2}\Re F(u+i\theta h_*)
               =-h_*^T\Re F''(u+i\theta h_*)h_*\ge0.
 \tag{19}
\]
Thus every joining path in (16) has rate at most
\(M-\min(\delta_f,\mu d^2/2)\). Independent intermediate
heights are not inserted into this convexity argument. The small
half-grid shifts cost an arbitrarily small rate tolerance.

## 4. All remaining lattice currents reduce to eight maxima

Every product in \(\mathcal A_N\) containing some \(V_j\)
has a real coordinate on a face. Equations (11)--(15), including
the penalties in every other alias or vertical coordinate, bound
its rate by \(\max_{\partial C}E\). The two sides of each
vertical difference may now be bounded separately. Their finite
number, lengths, row symbols and powers of \(N\) cost only a
polynomial. Thus the same physical-face gap pays every such term.

The remaining products use only \(I_j,A_j^-,A_j^+\). Apart
from the all-zero choice, there are \(3^4-1=80\) height
vectors. For each one keep a nonzero component and reset the
others to zero in (12). It follows that the largest containing
rate of all 80 products is exactly
\[
 B_*:=\max_{j,\pm} B_{j,\pm},\qquad
 B_{j,\pm}=\max_{u\in C}
       \{\Re F(u+ih_{j,\pm}e_j;x_0,-2)-2\pi|h_{j,\pm}|\}.
 \tag{20}
\]
The reverse inequality holds because all eight single-height
vectors are themselves among the 80. These are the original
prepared heights (3), with all four real coordinates free.
The functions being maximized are strictly concave by the
whole-rectangle Hessian bound. A tangent at any point of the
full box therefore bounds each globally, provided all four
signed support terms are retained. No chosen trial point is
assumed to be a maximizer.

## 5. Sufficient whole-source theorem and remaining obligations

**Theorem 2.** Suppose the following three facts hold at the fixed
original parameters \((x_0,-2)\):

1. The original phase (4) has a critical point \(z_*\) strictly
   inside \(\mathscr R\), with its original zero logarithmic
   lifts. It suffices to identify a regular preimage in the
   critical-curve equations with the same endpoint chamber filter
   and these strict coordinate bounds: the zero-lift proof extends
   to (3), as in the typed-height theorem.
2. The prepared physical bound satisfies \(P_*<M\), where
   \(P_*\) is (7) and \(M=\Re F(z_*;x_0,-2)\).
3. The eight prepared alias bounds satisfy \(B_*<M\), with
   \(B_*\) given by (20).

Then the complete original finite source has, on a fixed neighborhood
of \((x_0,-2)\),
\[
 G_{34,N}(y,w)=\kappa^3N^{-1}\mathcal B(y,w)
                   e^{N\Phi(y,w)}(1+O(N^{-1})),
 \tag{21}
\]
where
\[
 \Phi(y,w)=F(z_*(y,w);y,w),\qquad
 \mathcal B(y,w)=
 \frac{(2\pi)^2 b_{\mathrm{cap}}(z_*(y,w);y,w)}
      {\sqrt{\det(-F''(z_*(y,w);y,w))}}\ne0.
 \tag{22}
\]
The determinant branch is the one determined by the original
oriented horizontal Gaussian. Both functions are holomorphic;
the asymptotic holds at both parities and with all fixed ordinary
and Fourier derivatives on a smaller neighborhood. In particular
there are uniform positive upper and lower constants multiplying
\(N^{-1}e^{N\Re\Phi}\) there, for all sufficiently large \(N\).

*Proof.* The original Hessian proves uniqueness, nondegeneracy
and holomorphic continuation of the identified root. At the base
parameters its critical-height plane has a unique real maximum,
with a strict quadratic loss away from \(\Re z_*\).
The local four-dimensional Gaussian in the source theorem is
therefore the leading term of \(\mathcal M_N\). Its power is
\(N^4N^{-3}N^{-2}=N^{-1}\), and its coefficient is exactly
(22). The other part of that horizontal integral is exponentially
smaller by the same concavity.

The physical-tail theorem, with a sufficiently small rate
tolerance, pays \(\mathcal P_N\). Equations (18)--(19) pay
\(\mathcal J_N\). Section 4 pays every term in
\(\mathcal A_N\): the vertical ones use the face gap and
the horizontal ones the eight alias gaps. The exact finite
denominators in (15) are uniformly bounded away from zero for
large \(N\); the remaining polynomial losses are absorbed by
the strict exponential gaps. Thus (17) has precisely the leading
term just computed.

All inequalities have strict room on compact sets. Shrinking a
fixed parameter neighborhood preserves the physical upper bound,
the original row interpolation, the gradient strips and the
comparisons with \(\Re\Phi(y,w)\). The continued local
critical cycle gives the holomorphic Gaussian coefficient; its
boundary deformation remains within the same gapped rectangle.
This proves (21) uniformly. Cauchy estimates on nested fixed
parameter neighborhoods give the fixed-derivative conclusion.
Nonvanishing of the symbol and determinant then gives the
two-sided bound. \(\square\)

The new implication is a complete finite-source criterion for this
particular prepared two-letter cap. No values in (7) or (20),
and no prepared critical action, have been evaluated here. The
completed paired-kernel margins are not premises for these new
comparisons. Even after (21) is established, its neighborhood is
local in the outgoing Fourier variable: a full outgoing-period
envelope and a propagated whole-message remainder would still be
needed for arbitrary attachments. No whole mixed-word source,
short-partial-filling stability, or new knot-family theorem is
asserted.
