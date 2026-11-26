# A direct reflected-source bound at the endpoint seam

Research deduction, 7 November 2026. The original endpoint polynomial
has arbitrarily small exponential growth on sufficiently small fixed
complex neighborhoods of \(Y=1\) and the complete ordinary color.
The proof uses its literal finite source, exact factorial reflection,
and a tall contour for the middle Newton indices. It does not use
the asserted all-index continuous packet or extrapolate a physical
coefficient asymptotic through an unsupported interval.

This is an upper bound, not a nonzero asymptotic or a normalized
action at the seam. Both parities and every original Newton row
are retained.

## 1. Statement and independent source inputs

For \(N\ge2\), retain
\[
 \begin{gathered}
 q=e^{\pi i/N},\qquad r=q^{-2},\qquad
 P_l=(r;r)_l,\qquad S_l=|P_l|,\\
 e_l(w)=S_l^{-2}\prod_{\nu=0}^{l-1}
                \left(2\cos\frac{(2\nu+1)\pi}{N}-w\right),\\
 H_N(w,Y)=\sum_{l=0}^{N-1}
             \frac{(-q)^{-l}e_l(w)}{P_l}(Y;r)_l .
 \end{gathered}                                                   \tag{1}
\]
At \(Y=1\), the exact value is \(H_N(w,1)=1\).
That value alone is not used to control a neighborhood.

**Theorem 1.** For every \(\eta>0\), there are fixed
\(\rho,\zeta>0\) such that
\[
 \sup_{\substack{|w+2|\le\rho\\|Y-1|\le\zeta}}
   |\partial_w^k\partial_Y^m H_N(w,Y)|
          \le C_{\eta,k,m}N^{B_{\eta,k,m}}e^{\eta N}
                                                               \tag{2}
\]
for every fixed \(k,m\ge0\), uniformly along both level parities.
The radii can be chosen once for all fixed derivative orders,
by proving the undifferentiated bound on larger disks and then
halving those radii.

We use only the following independent source facts:

* the canonical sine factorial and its exact reflection from
  [factorial interpolation](exact_factorial_interpolation_and_complex_contours.md)
  and [uniform reflected bounds](research_uniform_factorial_and_boundary_decay.md);
* the exact Newton interpolation in
  [the physical coefficient theorem, equations (8)--(9)](research_complete_boundary_coefficient_asymptotic.md);
* the whole-index zero-safe finite Newton bounds in
  [the color tube theorem, equations (5)--(7)](research_mixed_newton_color_tubes.md);
* the literal product collar in
  [the seam majorants, equations (1)--(3), (7)](research_mixed_endpoint_seam_majorants.md).

The later polynomial-collar conclusion and its continuous
compact-index premise are not inputs.

## 2. The two physical end ranges

Let
\[
 \mathcal V(u)=2\int_0^u\log(2|\cos\pi v|)\,dv-2J(u),
                   \qquad 0\le u\le1,
                                                               \tag{3}
\]
where \(J(u)=\int_0^u\log(2\sin\pi v)\,dv\) on the real
unit interval. The cited Newton source bounds give
\[
 |e_l(w)|\le C_\rho N^{B}
               e^{N\{\mathcal V(l/N)+\sqrt\rho\}}
                         \qquad(|w+2|\le\rho\le1).
                                                               \tag{4}
\]
The function \(\mathcal V\) is continuous,
\[
 \mathcal V(0)=\mathcal V(1/2)=0,\qquad
 \mathcal V(u)\le0\quad(1/2\le u\le1).
                                                               \tag{5}
\]
In particular
\[
 \sup_{u\in[0,2d]\cup[1/2-2d,1]}\mathcal V(u)
                         \longrightarrow0\quad(d\downarrow0).
                                                               \tag{6}
\]
No complete-color zero is divided out in (4).

For \(|Y-1|\le\zeta\), the exact product bound is
\[
 \frac{|(Y;r)_l|}{S_l}
     \le\frac{\zeta N}{4}e^{N\omega(\zeta)}
                           \quad(1\le l<N),
 \qquad
 \omega(\zeta)=\log(1+\zeta/2)
           +\frac{\zeta}{2}\log(1+2/\zeta),
                                                               \tag{7}
\]
with \(\omega(\zeta)\to0\).
Indeed \((Y;r)_l=(1-Y)p_{l-1}(Y)\),
\(|p_{l-1}(Y)|\le S_{l-1}e^{N\omega(\zeta)}\), and
\(S_l/S_{l-1}=2\sin(\pi l/N)\ge4/N\).
The \(l=0\) term is exactly one.

Choose a small fixed \(d\in(0,1/8)\), and put
\[
 L_N=\lceil Nd\rceil,\quad
 K_N=\lfloor N(1/2-d)\rfloor+1,\quad
 \ell_N=\frac{L_N-1/2}{N},\quad
 u_N=\frac{K_N-1/2}{N}.
                                                               \tag{8}
\]
For large \(N\), the two cuts lie in
\([d/2,1/2-d/2]\). Every index outside
\(L_N\le l<K_N\) belongs to the set in (6).
Equations (4)--(7) consequently bound the complete physical
end contribution by a polynomial times
\[
 \exp N\left\{
   \sup_{[0,2d]\cup[1/2-2d,1]}\mathcal V+
                               \sqrt\rho+\omega(\zeta)\right\}.
                                                               \tag{9}
\]
This rate can be made arbitrarily small. It includes all
indices above \(N/2\), at even as well as odd levels, and
includes \(l=N-1\). No continuation theorem is used here.

## 3. Exact reflection of the retained finite source

Write \(Y=e^{2\pi ie}\), using the logarithm near \(Y=1\),
and let \(G_N\) be the canonical sine factorial. The original
factorial recurrence gives the finite identity
\[
 H_N(w,e^{2\pi ie})
   =G_N(Ne)\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}
                    {S_lG_N(Ne-l)} .
                                                               \tag{10}
\]
It can be verified term by term from (1); no asymptotic
assertion about this continuation is needed.

The exact midpoint reflection formula is
\[
 \frac1{G_N(Nv-1/2)}
       =\frac{2\cos(\pi Nv)}{N}G_N(-Nv-1/2).
                                                               \tag{11}
\]
At \(z=Ne-l\), this gives
\[
 \frac1{G_N(Ne-l)}
       =-\frac{2(-1)^l\sin(\pi Ne)}N
                            G_N(l-Ne-1).
                                                               \tag{12}
\]
Also
\[
 \chi_N(e):=\frac1{G_N(-Ne-1)}
               =-\frac{2\sin(\pi Ne)}N G_N(Ne).
                                                               \tag{13}
\]
The reciprocal defining \(\chi_N\) is holomorphic on a fixed
small complex neighborhood of zero. It vanishes at \(e=0\).
Thus (10)--(13) give, on the middle range of (8), exactly
\[
 H_N^{\rm mid}(w,e^{2\pi ie})
       =\chi_N(e)\sum_{l=L_N}^{K_N-1}
                                 \mathscr T_N(l/N;e,w),
                                                               \tag{14}
\]
where
\[
 \mathscr T_N(u;e,w)=
 e^{i\pi N(e+1)u}\,
 \mathcal E_N(u,w)
              \frac{G_N(N(u-e)-1)}{G_N(Nu)} .
                                                               \tag{15}
\]
Here \(\mathcal E_N(l/N,w)=e_l(w)\) is the exact original
Newton interpolation. The sign \((-1)^l\) in (12) is the
factor \(e^{i\pi Nu}\) in (15).
At the sampled middle indices and small \(e\), all factors
on the right of (14) are regular. Consequently (14) remains
valid through zeros of \(\chi_N\); there is no division by
that carrier.

For clarity the exact interpolation may be written with
\(w=-2\cos\theta\) and \(c_N=(N-1)/2\):
\[
 \mathcal E_N(u,w)=
 \frac{N}{
 G_N(Nu)^2
 G_N(c_N-Nu+N\theta/(2\pi))
 G_N(c_N-Nu-N\theta/(2\pi))}.
                                                               \tag{16}
\]
It is even in \(\theta\), and hence holomorphic in \(w\)
near \(-2\). Fix any finite height \(A>0\).
On
\[
       d/2\le\Re u\le1/2-d/2,\qquad |\Im u|\le A,
                                                               \tag{17}
\]
all the arguments in (15)--(16) remain in their original
regular strips when \(e,w+2\) are sufficiently small.
The neighborhoods may depend on \(d,A\) but not on \(N\).

The regular factorial estimates bound (15), with a polynomial
prefactor, by the phase
\[
 \begin{split}
 \Phi(e,u,w)
   &=V(u,w)+J(u-e)-J(u)+i\pi(e+1)u,\\
 V(u,-2\cos\theta)
   &=-2J(u)-J(1/2-u+\theta/(2\pi))
                        -J(1/2-u-\theta/(2\pi)).
 \end{split}                                                    \tag{18}
\]
These are holomorphic functions on the fixed compact source
chart (17). All order-one shifts in the factorial arguments
change only their symbols and polynomial factors.

The carrier itself has arbitrarily small exponential rate:
for every \(\epsilon>0\), on a sufficiently small fixed
\(e\)-disk,
\[
                         |\chi_N(e)|\le C_\epsilon N^B e^{\epsilon N}.
                                                               \tag{19}
\]
To see this directly, apply the zero-safe reciprocal midpoint
bound to \(v=-e-1/(2N)\) in (11). The original upper
exponent \(-\Re J_{\rm side}(v)\) tends uniformly to zero
as \(v\to0\). Changing \(v\) by \(1/(2N)\) costs
\(O(\log N/N)\), because the primitive has only the integrable
logarithmic singularity there. This includes every reciprocal
zero and both side branches. It does not estimate
\(\chi_N\) by dividing by \(\sin(\pi Ne)\).

## 4. The middle phase decreases along a tall contour

At \(e=0,w=-2\), put
\[
 V_0(u)=-2J(1/2-u)-2J(u),\qquad
 F_+(u)=V_0(u)+i\pi u,\qquad
 F_-(u)=V_0(u)-i\pi u.
                                                               \tag{20}
\]
These are the limiting phases of the exact source, not a
replacement of its vanishing carrier.
For \(0<x<1/2\), \(h>0\), the cotangent
\(\cot\pi(x+ih)\) has positive real part and negative
imaginary part. On the original branch,
\[
 V_0'(u)=2\Log\cot\pi u,\qquad
 \partial_h\Re F_+(x+ih)
       =-2\arg\cot\pi(x+ih)-\pi<0.
                                                               \tag{21}
\]
In particular this derivative has no hidden logarithmic lift.
The real phase decreases up each vertical line.

Its limiting value is zero. One direct derivation, for
\(z=e^{2\pi iu}\) with \(|z|<1\), is
\[
 F_+(u)=\frac{i\pi}{4}
          -\frac{i}{\pi}\{\operatorname{Li}_2(z)
                                      -\operatorname{Li}_2(-z)\}.
                                                               \tag{22}
\]
This follows by integrating
\(\Log(2\sin\pi u)=i\pi(1/2-u)+\Log(1-e^{2\pi iu})\)
in the upper half-strip and using the conjugate lower formula
for \(1/2-u\). The constants are fixed by the original
primitive; the remaining constant in (22) is purely imaginary.
The absolutely convergent power series gives
\[
 |\Re F_+(x+ih)|
       \le\frac{2e^{-2\pi h}}{\pi(1-e^{-4\pi h})}
                 \longrightarrow0\quad(h\to+\infty),
                                                               \tag{23}
\]
uniformly in \(x\). Equations (21)--(23) also show
\[
                0\le\Re F_+(x+ih)\le V_0(x).
                                                               \tag{24}
\]
At height zero this means its continuous limit.
Reflection gives
\[
 F_-(x-ih)=\overline{F_+(x+ih)},\qquad
 \Re F_+(x-ih)-2\pi h=\Re F_+(x+ih).
                                                               \tag{25}
\]
The second equality is the lower-alias identity needed below.
Thus the rapidly varying phase \((-1)^l\) is retained
coherently; an absolute estimate of its real middle rows
would not give (23).

## 5. Exact currents and their bounds

Take the rectangle
\(\mathcal R_N=[\ell_N,u_N]+i[-A,A]\), with positive
orientation, where \(A>0\) is fixed before the parameter
neighborhoods are chosen. The exact residue formula is
\[
 \begin{split}
 \sum_{l=L_N}^{K_N-1}\mathscr T_N(l/N)
    &=N\int_{\ell_N}^{u_N}\mathscr T_N(v)\,dv+\mathcal A_N,\\
 \mathcal A_N
    &=\frac{N}{2i}\left\{
       \int_{\partial\mathcal R_N^+}
            \mathscr T_N(u)[\cot(\pi Nu)+i]\,du+
       \int_{\partial\mathcal R_N^-}
            \mathscr T_N(u)[\cot(\pi Nu)-i]\,du\right\}.
 \end{split}                                                    \tag{26}
\]
Each upper or lower outer boundary includes its two vertical
halves. The real segment is not included in either.
This is the ordinary residue identity with the two constants
subtracted; the constant mode has density \(+N\).

On a half-grid side the two alias kernels have modulus at
most \(2e^{-2\pi N|\Im u|}\) on their respective halves.
At the two horizontal edges the constant may be taken as
four for all sufficiently large \(N\).
Now move the real main segment in (26) to height \(+A\),
retaining both unweighted vertical connectors.
At the limiting parameters \(e=0,w=-2\), (21)--(25) give:

* both main connectors have rate at most
  \(\max\{V_0(\ell_N),V_0(u_N)\}\);
* the upper vertical aliases have no larger rate, since
  they carry the additional penalty \(-2\pi h\);
* the lower vertical aliases have exactly the same
  phase bound as the reflected upper phase in (25),
  and thus have the same endpoint bound;
* the raised main and lower horizontal alias both have
  rate bounded by the right side of (23) at \(h=A\);
  the upper horizontal alias has an additional
  \(-2\pi A\) penalty.

All three horizontal pieces and all the vertical pieces
of this exact identity have therefore been included.
In particular the lower alias is not dropped on the grounds
that the main contour was raised.

Here is a uniform choice of parameters proving the required
bound. First choose \(d\) so small that the supremum in (6)
is less than \(\eta/16\). This also makes both limiting
cut rates less than \(\eta/16\).
Next choose a fixed \(A\) so large that the right side of
(23) is less than \(\eta/16\).
On the resulting fixed compact rectangle, holomorphy of
(18) gives sufficiently small fixed neighborhoods of \(e=0\)
and \(w=-2\) such that
\[
              |\Re\{\Phi(e,u,w)-F_+(u)\}|<\eta/16.
                                                               \tag{27}
\]
The same inequality applies to the lower-alias phase after
subtracting its exact \(2\pi|\Im u|\) penalty.
Every integral in (26), after moving the main, consequently
has rate at most \(\eta/8\), with a uniform polynomial
prefactor. Their lengths, the densities \(N,N/(2i)\), and
the fixed finite number of contours cost only polynomial
powers. Choose the \(e\)-disk further so that (19) holds
with \(\epsilon=\eta/16\). Equation (14) then bounds the
complete middle contribution with rate at most \(3\eta/16\).

Finally decrease the color and \(Y\) disks so that
\(\sqrt\rho+\omega(\zeta)<\eta/8\), their logarithmic
coordinate lies in the chosen \(e\)-disk, and (27) remains
valid. Equation (9) bounds the two physical ends with rate
less than \(3\eta/16\) as well. Their sum with the middle
source proves the undifferentiated assertion of (2), with
ample reserve. Finitely many small levels are absorbed
into its constant.

The source is a polynomial in both \(w\) and \(Y\).
Prove the just-stated bound on fixed disks of twice the
final radii and apply Cauchy's formula on the smaller
disks. This proves every fixed joint derivative with
the same exponential rate. The proof used no level-parity
restriction: the high rows were bounded by (9), even when
an odd-level complete-color factor vanishes and its normal
derivative does not. This completes Theorem 1.

## 6. Scope of the repair

Equation (2) supplies an independent proof of the small-seam
upper bound near \(Y=1\), including fixed ordinary normals.
It can be used wherever only that bound is needed.
It does not prove the continuous endpoint packet on every
compact subinterval of \((0,1/8)\), or identify the
dominant action of \(H_N\) at a fixed nonzero small angle.
The source gap in that broader continuation claim remains
distinct from this local result.

The proof also does not turn \(H_N(w,1)=1\) into a uniform
relative approximation to one. The small neighborhoods in
(2) depend on the requested exponential tolerance, and
the theorem asserts no nonvanishing there.

## 7. Every real ordinary color and its fixed normal derivatives

**Corollary 2.** For every \(\eta>0\), a sufficiently small fixed
\(\zeta>0\) satisfies
\[
 \sup_{\substack{-2\le w\le2\\|Y-1|\le\zeta}}
   |\partial_w^k\partial_Y^m H_N(w,Y)|
       \le C_{\eta,k,m}N^{B_{\eta,k,m}}e^{\eta N}
                                                               \tag{28}
\]
for all fixed \(k,m\ge0\), at both level parities.
As in Theorem 1, one radius suffices for all fixed orders.

*Proof.* The physical end argument already holds uniformly at
every real color. Indeed the Newton entropy bounds give
\(V_\theta(u)\le V_0(u)\) below \(1/2\), and
\(V_\theta(u)\le0\) above it, including all product zeros.
Thus (6)--(9) apply without the complex-color excess.

For the middle contour, let \(w=-2\cos\theta\),
\(-\pi\le\theta\le\pi\). The exact interpolation (16) is
holomorphic in \(u\) on the whole rectangle (17).
The two midpoint arguments have normalized real parts
\[
 -1/2+d/2\le
       \Re(1/2-u\pm\theta/(2\pi))\le1-d/2.
                                                               \tag{29}
\]
Thus their reciprocal factorials stay in the original
holomorphic reflected strip, even when they vanish.
No positive-strip-only formula is asserted at those zeros.

Apply [the uniform factorial theorem, Lemma 2 and equation (6)](research_uniform_factorial_and_boundary_decay.md)
to this exact Newton interpolation. Its complete real-color
upper exponent \(\mathfrak b(u,\theta)\) obeys
\[
 \begin{split}
 |\mathcal E_N(u,-2\cos\theta)|
       &\le C N^B e^{N\mathfrak b(u,\theta)},\\
 \mathfrak b(v+ih,\theta)
       &\le \Re V_0(v+ih)
          -\frac{\sin(2\pi v)}{4\pi\cosh^2(\pi h)}
                                      (1-\cos\theta)
        \le\Re V_0(v+ih).
 \end{split}                                                    \tag{30}
\]
The constants are uniform over the fixed rectangle and the
whole real color period. All remaining factors in (15) and
the carrier (13) are independent of this color.
For small \(e\), their change from the limiting phase is
uniformly small on that rectangle. Consequently every tall
current and both main connectors have the same upper rates
as in Section 5, uniformly in \(\theta\). Together with the
two physical end ranges this proves (28) for \(k=m=0\).

For each fixed complex \(Y\) in the resulting disk, the
**complete finite polynomial** \(w\mapsto H_N(w,Y)\) has
degree at most \(N-1\). Markov's inequality on \([-2,2]\)
therefore costs only a power of \(N\) for each fixed
ordinary derivative. For complex coefficients one may
apply the real inequality to real and imaginary parts.
Markov is applied after bounding the complete source,
not to the off-grid factorial interpolation (16).
Finally use Cauchy's formula in \(Y\) on a smaller fixed
disk to obtain the mixed derivatives. This preserves the
exponential rate and every physical normal direction.
\(\square\)

This all-real conclusion is likewise only a small-seam
upper bound. It neither adds a continuous compact-index
packet nor transfers a nonzero complete-color coefficient
to another ordinary observation.
