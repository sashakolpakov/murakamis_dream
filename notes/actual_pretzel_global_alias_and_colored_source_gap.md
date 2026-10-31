# A global alias bound and the full original colored-source gap

29 October 2026. The entire original \(RP\) band has the uniform
faithful-Hermite upper rate

\[
 B=\tfrac12\log(4+\sqrt{15})
       <j_0=\frac{v_8}{\pi}.
 \tag{1}
\]

The proof uses the exact short-band coefficients, monic physical
continuants, and an elementary spectral ellipse for their recurrence.
It retains the value AND first normal coefficient at every double
Casimir node. It requires no ordinary-color unitarity, Laurent
positivity conjecture, or discarded endpoint sector.

Combining this bound with the
[proved global low-core bound](actual_pretzel_global_core_spectral_gap.md)
gives a strict original-source gap outside every fixed complete-color
corridor, over the ENTIRE auxiliary-color cube, for every fixed odd
width \(s\geq25\). More generally the exact sufficient condition is
\(A_s>(s-1)j_0+B\). This supplies a global-color input for long
fillings; the selected cusp-corridor filling asymptotic and its
peripheral identification remain separate.

## 1. Rewrite the exact short band before estimating it

Use \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(M=\lfloor d/2\rfloor\). Let \(p_l\) be the MONIC physical
middle-degree continuant:

\[
 p_0=1,\quad p_{-1}=0,\qquad
 p_{l+1}(z)=(z-D_l)p_l(z)-a_{l-1}^{\,2}p_{l-1}(z),
 \tag{2}
\]
\[
 D_l=4qQ^l-q(1+Q)Q^{2l},\qquad
 a_{l-1}=-(1-Q^l)^2.
\]

Thus \(p_l=(a_0\cdots a_{l-1})f_l\). A bar on a polynomial
denotes coefficient conjugation at this root. For
\(1\leq h\leq\lfloor N/2\rfloor\), define the literal short
polynomial by the same finite formula as the cusp split:

\[
 P_{N,h}=
 \sum_{t=1}^{h}(-1)^{N-t-h}
       \frac{s_{t-1}^2s_{t+h-1}}{s_{2t-1}s_{h-t}}
                                                  \bar f_{t-1}.
 \tag{3}
\]

The endpoint \(h=N/2\) at even \(N\) is allowed in (3): the
largest factorial index is \(2h-1=N-1\). It is needed for the
actual middle auxiliary color, which has no low core.

All small denominators in (3) cancel in the following exact
polynomial identity:

\[
 \boxed{\quad
 (-1)^{N+h-1}P_{N,h}(z)=
 \sum_{l=0}^{h-1}(-1)^l
 q^{3l^2+4l+1-2hl-h}
      {h+l\brack 2l+1}_Q\,\bar p_l(z).
 \quad}                                                \tag{4}
\]

Indeed \(s_a=i^a q^{-a(a+1)/2}F_a\). In the term \(t=l+1\),
the factorial ratio not containing \(s_l^2\) becomes its Gaussian
coefficient with the indicated phase. Also
\(F_l^2\bar f_l=(-1)^lQ^{l(l+1)}\bar p_l\).
These two phase simplifications give (4), including its sign.
No factorial index in (4) reaches \(N\), and the Gaussian can
equivalently be regarded as its finite polynomial.

## 2. A uniform monic-continuant bound with all source endpoints

The required estimate is

\[
 \limsup_{N\to\infty}\ 
 \max_{0\leq l\leq M}\ 
 \frac1N\log\left(6^{-l}
                 \max_{z\in[-2,2]}|p_l(z)|\right)\leq0.
 \tag{5}
\]

The initial vector in (2) is exactly \((p_0,p_{-1})=(1,0)\).
Its coefficients have no singular endpoint. They are uniformly
smooth functions of \(u=\pi l/N\), \(0\leq u\leq\pi/2\),
with uniform \(O(1/N)\) error from their frozen classical values.

Put \(V=e^{2iu}\). The eigenvalues of the frozen companion are
\(V\lambda\), where

\[
 \lambda^2-d_z\lambda+a^2=0,
 \qquad d_z=zV^{-1}-4+2V,\qquad a=4\sin^2u.
 \tag{6}
\]

Both roots lie STRICTLY inside \(|\lambda|=6\), uniformly for
\(0\leq u\leq\pi/2\), \(-2\leq z\leq2\). Here is an
elementary verification, avoiding a chosen eigenbasis.

For fixed \(a\leq4<6\), a root on \(|\lambda|=6\) makes
\(d_z=\lambda+a^2/\lambda\), the ellipse with semiaxes
\(6+a^2/6\) and \(6-a^2/6\). Both roots at \(d_z=0\) are
inside that disk. The same segment-continuity argument used for the
mixed-source ellipse therefore puts both roots inside whenever
\(d_z\) is in the interior of this ellipse.

The point \(d_z\) is affine in real \(z\), so convexity reduces
the check to \(z=\pm2\). For \(z=2\),
\(d_2=-2a\), and
\(2a<6+a^2/6\) because \(a<6\).
For \(z=-2\), put \(y=1-\cos(2u)\in[0,2]\), so
\(a=2y\), \(d_{-2}=-4+4i\sin(2u)\). The ellipse condition is

\[
 \frac{36}{(9+y^2)^2}
 +\frac{36(2y-y^2)}{(9-y^2)^2}<1.
 \tag{7}
\]

After multiplication by \((81-y^4)^2>0\), its positive slack
factors exactly as

\[
 (y^4+12y^2-36y+27)(y^4+24y^2-36y+135).
\]

The first factor equals
\((y-1)^2(y^2+2y+3)+12(y-4/3)^2+8/3>0\).
The second equals
\(y^4+24(y-3/4)^2+243/2>0\). This proves the uniform strict
root bound, including both index endpoints.

For completeness, this spectral statement genuinely bounds the
varying product in (2). Divide each frozen companion by 6. On
the compact \((u,z)\) set the matrices are uniformly bounded and
their eigenvalues have modulus at most 1. Cayley--Hamilton gives
\(\|B^L\|\leq L\|B\|+L-1\leq C L\), including double roots.
An exact block of fixed length \(L\) differs from the frozen
power by \(O_L(1/N)\), uniformly in \(u,z\). Choose \(L\) large
to make \(\log(CL)/L\) arbitrarily small, then choose \(N\)
large and concatenate the blocks. The two incomplete blocks have
bounded cost. This proves (5) uniformly in \(l,z\), without
adiabatic eigenvector transport or an uncontrolled endpoint factor.

## 3. A global bound for the entire alias, including the normals

At a unit root the finite Gaussian satisfies
\(|{h+l\brack2l+1}_Q|\leq{h+l\choose2l+1}\), by its elementary
Pascal polynomial expansion with nonnegative integer coefficients.
Consequently (4)--(5) give a sequence \(\epsilon_N\to0\),
independent of \(h\), with

\[
 \max_{[-2,2]}|P_{N,h}|
 \leq e^{\epsilon_NN}
      \sum_{l=0}^{h-1}{h+l\choose2l+1}6^l
 =e^{\epsilon_NN}U_{h-1}(4).
 \tag{8}
\]

The identity follows from the generating function
\(\sum_{h\geq1}\sum_{l<h}{h+l\choose2l+1}K^l t^{h-1}
 =[1-(K+2)t+t^2]^{-1}\).

The actual short polynomial has degree \(h-1\leq M\).
Complex Markov on \([-2,2]\) therefore bounds its derivative
by \((h-1)^2/2\) times its supremum. In the original faithful
Hermite norm, with normal scale \(N^{-2}\), this costs at most
\(9/8\). The literal crossing also has norm at most \(9/8\).
Thus the whole original alias obeys

\[
 \boxed{\quad
 \|R P_{N,h}\|_{\mathrm H}
 \leq\frac{81}{64}e^{\epsilon_NN}U_{h-1}(4)
 \leq\frac{81}{128\sqrt{15}}e^{\epsilon_NN}
                                 (4+\sqrt{15})^h.
 \quad}                                                \tag{9}
\]

It includes every value and every first normal coefficient. In
particular, uniformly for \(1\leq h\leq\lfloor N/2\rfloor\),

\[
 \limsup_N\frac1N\log\|RP_{N,h}\|_{\mathrm H}
                    \leq B=\tfrac12\log(4+\sqrt{15}).
 \tag{10}
\]

This is a source-compatible upper bound, not a claim that the alias
is polynomial, nor an asserted sharp asymptotic for it.

## 4. Every original auxiliary color is covered

For \(j>N/2\), put \(h=N-j\leq M\). The exact box is
\(z_{N,h}=c_{N,h}+RP_{N,h}\), with a zero alias at \(h=0\).
For \(1\leq j\leq\lfloor N/2\rfloor\), factorial complementation
in the literal high band gives

\[
 \mathscr R(R^{-1}L_j)=(-1)^N RP_{N,j}.
 \tag{11}
\]

This includes \(j=N/2\) at even \(N\). Thus no middle color,
normal channel or color endpoint is absent.

The [global core theorem](actual_pretzel_global_core_spectral_gap.md),
followed by complex Markov and the limit of its fixed radius
\(R\downarrow1\), gives the uniform bound

\[
 \limsup_N\frac1N\log
             \max_{0\leq h\leq M}\|c_{N,h}\|_{\mathrm H}
                                      \leq j_0.
 \tag{12}
\]

Apply (9),(12) to the original source
\(|\Phi_2(f)|\leq3N^3\|f\|_{\mathrm H}\). Any product term
with a nonempty alias set of size \(m\) has uniform upper rate

\[
 (s-m)j_0+mB\leq(s-1)j_0+B,
 \tag{13}
\]

since \(B<j_0\). This applies across the ENTIRE original color
cube, including low colors whose boxes are pure aliases.

Let \(A_s=V_s/(2\pi)\). Whenever

\[
 \boxed{\qquad g_s:=A_s-(s-1)j_0>B,\qquad}            \tag{14}
\]

all alias-containing original-source terms have a fixed exponential
gap from the complete geometric period. The finite subset expansion
costs at most \(2^s\), with \(s\) fixed.

Condition (14) holds for EVERY odd \(s\geq25\). Indeed the previous
elementary bound is \(g_s\geq j_0-\pi/[s\cos(\pi/s)]\).
Here is a rational check at the smallest stated width: use
\(\pi<22/7\),
\(G>1-1/9+1/25-1/49+1/81-1/121\),
\(\cos(\pi/25)>1-(22/175)^2/2\), and \(B<31/30\).
These give a strictly positive rational lower margin greater than
0.00139. The last logarithmic bound follows by the first ten terms
of the exponential series at \(31/15\): their sum is greater than
\(4+\sqrt{15}\). Finally \(s\cos(\pi/s)\) increases with \(s\).

## 5. The full off-cusp original-source theorem

Fix an odd \(s\geq25\) and any \(0<\delta<1/2\). There is
\(\gamma_s(\delta)>0\) such that, uniformly over ALL actual
auxiliary colors \(1\leq j_i\leq N\) with at least one
\(j_i\leq N-\delta N\),

\[
 \boxed{\quad
 \limsup_N\frac1N\log
 \left|\mathcal A_{s,N}(j_1,\ldots,j_s)\right|
             \leq A_s-\gamma_s(\delta).
 \quad}                                                \tag{15}
\]

The limsup includes the maximum over those color tuples. To prove
it, if some color is at most \(N/2\), every term contains an alias,
so (13)--(14) give the gap. Otherwise all boxes have the exact
core-plus-alias split. Alias terms have the same gap; the all-core
term has a strict source gap by the global core theorem because at
least one deficit is at least \(\delta N\). Taking the smaller
of the two positive gaps proves (15).

In the exact original simultaneous filling sum, each fixed signed
twist kernel has polynomial total coefficient mass
\(\leq2N(1+|p_i|)\). Thus its ENTIRE off-cusp color contribution
is bounded by

\[
 |\chi_N|\prod_i2N(1+|p_i|)
     \exp\{N[A_s-\gamma_s(\delta)+o(1)]\}.
 \tag{16}
\]

All original \(\kappa\) factors are unit phases, and the original
\(\chi_N\) is displayed rather than absorbed. The estimate is
before any asymptotic deletion of filling normal data; their exact
Fourier--Hermite kernel is used with its proved total mass.

Equation (16) does not yet prove a filled-knot asymptotic. One must
still analyze the original coherent cusp-corridor sum, identify its
peripheral marking, and prove its selected contribution. The present
theorem removes the global-color obstruction for the stated broad
fixed-width family; it does not replace those remaining tasks by a
positive comparison invariant.
