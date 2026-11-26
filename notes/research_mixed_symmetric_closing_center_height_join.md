# Paying the center height join in the wider right inner contour

Private written finite-source deduction, 9 November 2026. The center
vertical from first height \(7/10\) to any height at most one is below
the actual symmetric closing budget. The proof retains the outgoing
real-angle loss and its quadratic height cost. The original shortened
edge envelope also extends to this imaginary first-angle axis, because
the outgoing leg supplies the strict boundary conditions.

This pays a specified inner joining current. It does not estimate the
other currents in a wider inner contour or complete the right outer
connection. No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test, or frozen-source edit is used.

## 1. Source, closing budget and statement

Use the original Newton polynomials, cutoff and full trace multiplier:
\[
 e_j(x)=S_j^{-2}\prod_{\nu<j}(c_\nu-x),\quad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\quad
 c_\nu=2\cos((2\nu+1)\pi/N),\quad
 U=\lfloor N/2\rfloor-1,
\]
\[
 \mathcal K_N^<(w,x)=\sum_{j=0}^Ue_j(w)e_j(x),\qquad
 K_N^<(t,u)=\mathcal K_N^<(-2\cos t,-2\cos u),
\]
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\quad
 \eta_N=(-1)^{N-1},\qquad C_{N,3}=e^{3\pi i(N-1)^2/(4N)}.
 \tag{1}
\]
The outgoing rectangle and first-height interval are
\[
 u=\beta-iK,\quad \pi/2\le\beta\le2\pi/3,\quad
 1/10\le K\le7/10,\qquad h_0=7/10\le h\le1 .
 \tag{2}
\]
Keep the calibrated original edge primitive \(\psi\). Put
\[
 R(h,u)=\Re\psi(-ih,0)+\Re\psi(-ih,u)-h,\qquad
 E(h,u)=\Re\psi(-ih,0)-h/2+K/2 .
 \tag{3}
\]
The cubic crossing is purely imaginary at \(t=-ih\); the final
\(-h\) in \(R\) is the original trace charge, not a new allowance.

Let \(u_g=\beta_g-iK_g\) be the actual symmetric \(343\) geometric
point, and retain
\[
 \Xi(u)=2S(u)+iu^2/\pi-iu,\qquad M_g=\Re\Xi(u_g).
 \tag{4}
\]
The adopted horizontal maximum theorem and the original inner floor
give the stronger elementary bound
\[
 M_g\ge\Re\Xi(\pi/2-iK_g)
       =2\Re S(\pi/2-iK_g)>\frac{321}{100}.
 \tag{5}
\]
Here \(17/30<K_g<7/10\), and the crossing and charge cancel in
real part at \(\Re u=\pi/2\). Thus (5) uses only the already proved
positive horizontal maximum and taller-strip action bound.
Define the half closing budget
\[
 \mathcal B(u)=\frac{M_g-(2\beta/\pi-1)K}{2}.
 \tag{6}
\]

For any \(h_1,h_2\in[h_0,1]\), let \(\gamma\) be the vertical segment
from \(-ih_1\) to \(-ih_2\), with that orientation, and set
\[
 I_N(w,u;\gamma)=
 -\frac{N^2C_{N,3}}{\pi i}\int_\gamma
 \sin t\,\mathcal K_N^<(w,-2\cos t)K_N^<(t,u)
                   e^{3iNt^2/(4\pi)}W_N(t)\,dt .
 \tag{7}
\]

**Theorem.** Uniformly in (2), in both parities and every such segment,
\[
 \sup_{w\in[-2,2]}\frac{N^2}{\pi}
 \int_\gamma\left|
 \sin t\,\mathcal K_N^<(w,-2\cos t)K_N^<(t,u)
                         e^{3iNt^2/(4\pi)}W_N(t)\right|\,|dt|
 \le C e^{N(\mathcal B(u)-1/50)}
 \tag{8}
\]
for all sufficiently large \(N\). In particular (8) bounds (7).
On a sufficiently small fixed complex neighborhood of \([-2,2]\),
the same assertion holds with gap \(1/100\). Every fixed incoming
ordinary derivative has that latter bound on a smaller neighborhood.

The exact cutoff in (1) is retained. Restoration of full edges is
a separate traced identity; (8) makes no pointwise replacement of
the complete kernel.

## 2. The original axis primitive and its finite edge envelope

Write
\[
 c=\cosh(h/2),\quad C=\cos(u/2),\quad A=c^2,\quad B=C^2,\quad
 D_0=A+B-AB,\quad W=AB/D_0 .
 \tag{9}
\]
On (2), \(A>1\), \(\Re B\le1/2\), and therefore
\[
 \Re D_0=A-(A-1)\Re B\ge(A+1)/2>1 .
 \tag{10}
\]
The original positive-series guards give
\[
 A<13/10,\quad |B|<23/20,\quad \Re(1/A)>10/13,\quad
 \Re(1/B)>20/23 .
\]
Moreover
\[
 \Im B=\tfrac12\sin\beta\,\sinh K>\sqrt3/40,\qquad
 \Re(1/W)>191/299,\qquad \Im(1/W)<0 .
 \tag{11}
\]
All strict distances can be made uniform on the compact box.
Thus the original \(y_*=\pi^{-1}\arctan\sqrt W\) lies in a compact
subset of the upper wire half-strip and is simple.

For the primitive used below its original derivatives are
\[
 d\psi=-\pi^{-1}(r_t\,dt+r_u\,du),\qquad
 r_t=\operatorname{arsinh}\{C\tan(t/2)\},\quad
 r_u=\operatorname{arsinh}\{c\tan(u/2)\},
\]
\[
 \psi_{uu}=-\frac{c}{2\pi C\sqrt{D_0}} .
 \tag{12}
\]
These are the calibrated principal returns, with the original
complete-edge constant. Their signs can also be checked directly
on this axis. The argument of \(r_t\) is
\(-iC\tanh(h/2)\), in the closed right lower quadrant; its imaginary
part has modulus less than one. The argument of \(r_u\) has positive
real part. More explicitly,
\(\Re C\le2^{-1/2}\cosh(7/20)<51/64\) and
\(\tanh(h/2)<1/2\), so the former imaginary modulus is
less than \(51/128\). Neither return meets its cut. Equation (10) fixes the
principal square root and identifies it in (12) by continuation.
At \(K=0\), these statements persist by the regular real limits.
They agree with the original complete primitive at \(h=0\) or
\(u=0\); no constant is inferred from the derivative alone.

Here is the finite-source justification at first angle zero. Apply
the construction of the adopted positive-first-angle wider-edge
theorem, with its first real angle tending to zero. The required
uniformity is verified afresh, not obtained by letting its
\(a_L\)-dependent constant tend to a limit:

- The incoming numerator cut has no open interior segment at
  first real angle zero. The outgoing cut retains the guards
  \(|e^{F_y}|^2<1999/2000\) for its nonnegative cut coordinate
  and \(|e^{F_y}|\le9/10\) for the negative coordinate. Its other
  cosine is the positive real \(\cosh h<8/5\), so every hypothesis
  of those original cut comparisons remains true.
- On the real wire the incoming force numerator is positive real,
  since \(\cosh h>1\). The outgoing force numerator has strictly
  positive imaginary part. Its original argument lies in
  \((0,\pi)\), giving the strict negative upward derivative on
  the entire open bottom.
- The left side is increasing from zero. The incoming right-side
  term is constant below \(h/(2\pi)\) and increasing afterwards.
  The outgoing term decreases before \(K/(2\pi)\) and has derivative
  at least \(\pi\) afterwards. Since \(h\ge K\), the summed right
  trace decreases to \(K/(2\pi)\) and then increases. Equal cut
  heights cause no exception. Both strict side sublevels are
  connected or empty.

The subharmonic envelope, its cut jumps, the simple critical point,
and its large-height growth are consequently the same hypotheses
of the full component/Jordan proof. The original critical charge
remains zero: (11) keeps the critical point away from the boundary,
the outgoing cut guard prevents a cut crossing, and the disappearing
incoming cut stays at the right boundary. Continue from a small
positive first angle, where the adopted theorem fixes the charge.
Its critical value is exactly the continuation in (12).

The resulting unweighted contour has rate at most
\(\max\{\Re\psi(-ih,u),(h+K)/2\}+\epsilon\).
Both complete alias paths can still use wire height two. Their
side constants are now
\[
 D_*=\frac{\beta K}{2\pi},\qquad e=(h+K)/2,\qquad
 e-D_*\ge h/2+K/6 .
 \tag{13}
\]
The original total dilogarithm error is below \(1/600\).
The physical endpoint rates remain \(0,e\). Thus the same fixed
collars bound both complete rational aliases, both external caps,
and both physical endpoint groups.

More precisely the canonical product \(T_N=B_N(y,t)B_N(y,u)\)
and the exact midpoint decomposition are those of equations
(17),(19)--(20) of that theorem. They retain the upper multiplier
\(N/(1-\zeta)\), lower multiplier \(N/(\zeta-1)\),
\(\zeta=e^{2\pi iNy}\), both signed external columns, and the sums
\(0\le j\le\lfloor N\alpha\rfloor\) and
\(\lceil N\gamma\rceil\le j\le U\). The two additional unweighted
caps still run from \(\alpha_N+ih_c\) to \(\alpha_N\), and from
\(\gamma_N\) to \(\gamma_N+ih_c\). All shifted real factorial
arguments remain in \([-1/3,5/6]\); the same zero-safe bounds apply.
A compact parameter cover gives uniform paths and constants.
Consequently, for every fixed \(\tau>0\),
\[
 |K_N^<(-ih,u)|\le C_\tau
   e^{N(\max\{\Re\psi(-ih,u),(h+K)/2\}+\tau)}
 \tag{14}
\]
uniformly on (2). No relative packet at the axis is needed.

## 3. Height and angle comparisons for the geometric sector

Both principal first-angle returns at \(t=-ih\) have imaginary
parts in \((-\pi/2,0)\). Equation (12) therefore gives
\[
 \partial_hR
   =-\pi^{-1}\Im\{r_0(-ih)+r_t(-ih,u)\}-1<0,\qquad
 r_0(t)=\operatorname{arsinh}\tan(t/2).
 \tag{15}
\]
Thus the maximum over the joining heights is at \(h=h_0\).

Fix this height and put \(c_0=\cosh(h_0/2)\). For each fixed \(K\),
the combined half-observation sector has derivative
\[
 \partial_\beta\{R(h_0,\beta-iK)+(\beta/\pi-1/2)K\}
  =\frac{K-\Re\operatorname{arsinh}
                 \{c_0\tan((\beta-iK)/2)\}}{\pi}<0 .
 \tag{16}
\]
For a complete written proof of the strict sign, put \(L=\cosh K<13/10\).
The positive quantity
\[
 X(\beta)=\Re\tan((\beta-iK)/2)
             =\frac{\sin\beta}{L+\cos\beta}
\]
has derivative \((1+L\cos\beta)/(L+\cos\beta)^2>0\) on the
stated interval. Hence \(X\ge1/L>10/13\).
If a principal return has argument with positive real part \(x\),
then \(\Re\operatorname{arsinh}(x+iy)\ge\operatorname{arsinh}x\):
write \(x=\sinh(\Re r)\cos(\Im r)\), where
\(\Re r>0\) and \(|\Im r|<\pi/2\).
Finally the positive series gives
\[
 \sinh(7/10)\le\frac{7/10}{1-49/600}
                =\frac{420}{551}<\frac{10}{13},
 \tag{17}
\]
since \(5460<5510\). Thus the return in (16) exceeds \(K\).
The maximum in \(\beta\) is at \(\pi/2\), where the added
outer term vanishes.

It remains to bound that endpoint. The original complete-edge
normalization is \(\psi(0,0)=2b_2\), \(b_2<7/12\), and
\(\psi_{tt}(t,0)=-\sec(t/2)/(2\pi)\). It follows that
\[
 \psi(0,\pi/2)\le2b_2-\pi/16,\qquad
 \psi(-ih_0,0)\le2b_2+\frac{49}{400\pi}.
 \tag{18}
\]
The second estimate follows by integrating
\(\arcsin(\tanh(h/2))/\pi\), whose derivative is at most
\(1/(2\pi)\).
For a real outgoing angle \(\beta\), the corresponding first-height
return is \(-i\arcsin(\cos(\beta/2)\tanh(h/2))\).
For \(0\le v\le1\) and \(z=\tanh(h/2)\),
\[
 \frac{d}{dh}\arcsin(v\tanh(h/2))
       =\frac{v(1-z^2)}{2\sqrt{1-v^2z^2}}\le v/2 .
 \tag{19}
\]
Indeed \((1-z^2)^2\le1-v^2z^2\).
Using \(\cos(\pi/4)<3/4\), this proves
\[
 \Re\psi(-ih_0,\pi/2)
       \le\psi(0,\pi/2)+\frac{147}{1600\pi}.
 \tag{20}
\]

Move next from \(\pi/2\) to \(\pi/2-iK\), keeping \(t=-ih_0\).
The initial height derivative vanishes because the outgoing
return is real. Along this segment \(|C|\ge1/\sqrt2\), and
\(\Re D_0=(c_0^2+1)/2>1\). The written
\(c_0<17/16\) bound gives
\[
 |\psi_{uu}|<\frac{17\sqrt2}{32\pi}
             <\frac{51}{64\pi}<\frac4{5\pi};
 \tag{21}
\]
the final comparison is \(255<256\).
Two integrations bound the increase by
\[
 \frac{2K^2}{5\pi}\le\frac{49}{250\pi}.
 \tag{22}
\]
Combining (18),(20),(22) and subtracting \(h_0\), then using
\(\pi>3\), yields
\[
 \begin{split}
 R(h_0,\pi/2-iK)
 &<\frac{49}{30}-\frac{\pi}{16}+\frac{3283}{8000\pi}\\
 &<\frac{37983}{24000}
       =\frac85-\frac{139}{8000}.
 \end{split}
 \tag{23}
\]
Equations (15)--(16) prove this same upper bound for
\(R(h,u)+(\beta/\pi-1/2)K\) everywhere in (2).

## 4. The endpoint sector and the full finite joining current

The first complete-edge height derivative is less than \(1/2\).
Thus \(\partial_hE<0\). Equations (18) and \(K\le7/10\) give
\[
 \begin{split}
 E(h,u)+(\beta/\pi-1/2)K
 &\le \psi(-ih_0,0)-7/20+K/2+K/6\\
 &<\frac76+\frac{49}{1200}+\frac7{60}
   =\frac{1589}{1200}<\frac43
       <\frac{37983}{24000}.
 \end{split}
 \tag{24}
\]
Consequently (5),(6),(23),(24) imply the uniform two-sector margin
\[
 \max\{R(h,u),E(h,u)\}
      <\mathcal B(u)-\frac{179}{8000}.
 \tag{25}
\]
This comparison retains the outer crossing and charge in (6).

For real incoming \(w\), the original full-period slit theorem gives
\[
 |\mathcal K_N^<(w,-2\cos(-ih))|
    \le C_\tau e^{N(\psi(-ih,0)+\tau)}
 \tag{26}
\]
uniformly in \(h\in[h_0,1]\) and \(w\in[-2,2]\).
The spectral arguments form a fixed compact set strictly below
\(-2\), so that theorem is directly eligible.
At \(t=-ih\), the crossing has modulus one, and
\[
 |W_N(-ih)|\le
       e^{-Nh}(1-e^{-Nh_0})^{-2}.
 \tag{27}
\]
The sine and all joining lengths are uniformly bounded.
Equations (14),(25)--(27) estimate the complete integrand of (7),
including every charge of its original denominator.
Choose \(\tau=1/2000\) in each edge bound and spend \(1/1000\)
on all polynomial costs, including \(N^2/\pi\).
The remaining reserve after gap \(1/50\) is
\[
 \frac{179}{8000}-\frac2{1000}-\frac1{50}
                         =\frac3{8000}>0 .
 \tag{28}
\]
This proves (8), including the absolute-integral version and
either orientation.

The exact integrand is a polynomial of degree at most \(U<N/2\)
in \(w\). Apply filled Bernstein-ellipse continuation pointwise
in \(t,u\) to the all-real integrand bound furnished by
(14),(25)--(27), before integrating in \(t\), using an arbitrarily
small fixed ellipse parameter. Absorb its finite polynomial
factor and lose less than \(1/100\) of the gap. This yields the
claimed fixed ordinary neighborhood version. Cauchy's formula
on a smaller neighborhood gives every fixed incoming derivative.
No variable-color relative packet is being continued.

Whenever a proposed wider inner contour has a critical depth
between \(7/10\) and one, its center joining vertical is one
of the segments covered by (8). The theorem does not locate
that critical point, bound the remaining signed horizontal,
or pay the right outer connection. It is an estimate of the
literal two-short current, with its original parity cutoff,
and is compatible with separately proved traced edge deletions.

## Frozen source bindings

- Wider positive-first finite edge, original charge, cut bounds,
  side geometry and complete interpolation/alias/cap inventory:
  f3f9cdca2307f100a5766638ae91e329be5c7f372ac9b303ede0a28c9953e22f.
- Original signed edge primitive, second derivatives and normalization:
  01630dd45f907e7d116fc8d51fed0ef00e13176f379b5ce1ab0186403cd1a94c.
- Complete first-short and all-real outside-period slit upper bound:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Original taller cubic action and \(s>321/200\) on its lower rectangle:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Actual symmetric horizontal maximum and unchanged closing phase:
  f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.
