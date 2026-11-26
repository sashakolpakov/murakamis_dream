# The upper log cut in the original finite Cauchy period

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The finite Cauchy representation of the centered source has a useful
explicit upper-cut estimate. We choose an interpolation that matches
every prescribed wall value and retains its nonperiodic last arrow.
The difference of its two sides along the upper logarithmic cut has
integral \(O(N^{-1})\). The half-step in the sampling nodes is kept,
so there is no cotangent pole or finite-part subtraction at the cut's
initial point.

The full contour identity below still contains a lower contour.
No estimate for that term, and no global growing-packet transport,
is proved here.

## 1. The original wall source and a specified interpolation

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\quad D_N(t)=1-\eta t^N.
 \tag{1}
\]
Write \(\mathbb D=\{w\in\mathbb C:|w|<1\}\).
Powers of \(q\) mean the displayed exponentials. The original tensor
\(\mathcal C_N(x,y,z)\) and its normalization are
\[
 \widehat{\mathcal C}_N
       =\frac{\mathcal C_N}{D_N(x)D_N(y)D_N(z)}.
 \tag{2}
\]
All variables lie in the unit disk unless otherwise specified.
The wall theorem gives, at \(u_j=(j+1/2)/N\),
\[
 \frac{\mathcal C_N(-e^{2\pi iu_j},y,z)}{D_N(y)D_N(z)}
 =\frac{\kappa}{\sqrt N}
       \frac{(Q;Q)_j(Qyz;Q)_j}
            {(-qy;Q)_{j+1}(-qz;Q)_{j+1}},
 \tag{3}
\]
and exactly
\[
 \widehat{\mathcal C}_N(x,y,z)
   =\frac1N\sum_{j=0}^{N-1}
     \frac{\mathcal C_N(-e^{2\pi iu_j},y,z)}
          {D_N(y)D_N(z)(1+x e^{-2\pi iu_j})}.
 \tag{4}
\]
These are the full original source values, with their repeated-root
data and their original Frobenius closing.

Let \(G_N(s)\) be the canonical sine factorial defined by its
convergent Gamma product in the exact factorial theorem. It is
holomorphic and nonzero on \(-1<\operatorname{Re}s<N\), is real
under coefficient conjugation, and satisfies
\[
 G_N(0)=1,\quad
 G_N(s+1)=2\sin\frac{\pi(s+1)}N\,G_N(s),\quad
 G_N(s)G_N(d-s)=N.
 \tag{5}
\]
Use its marked complex factorial
\[
 F_N(s)=e^{-\pi is/2+\pi is(s+1)/(2N)}G_N(s).
 \tag{6}
\]
Then \(F_N(j)=(Q;Q)_j\), and
\[
 F_N(s+1)=(1-Q^{s+1})F_N(s),\qquad
 F_N(s+N)=(1-e^{2\pi is})F_N(s).
 \tag{7}
\]
The second relation is obtained by multiplying the first \(N\) times.

The regular products will have their own explicit interpolation.
For \(|a|<1\) and \(|az|<1\), define
\[
 \mathcal E_a(z)=
   \exp\!\left\{\frac1N\sum_{k=0}^{d}k
                                      \Log(1-Q^{k+1}az)\right\},
\]
with logarithms anchored at \(az=0\). Set
\[
 P_a(s)=\frac{\mathcal E_a(Q^s)}{\mathcal E_a(1)}
       \exp\!\left\{\frac{s}{N}
                          \Log(1-a^Ne^{2\pi is})\right\}.
 \tag{8}
\]
This is holomorphic and nonzero wherever \(|aQ^s|<1\).
The finite-product norm and reindexing give
\[
 \frac{\mathcal E_a(Qz)}{\mathcal E_a(z)}
      =\frac{1-Qa z}{(1-a^Nz^N)^{1/N}}.
 \tag{9}
\]
Consequently
\[
 \begin{gathered}
 P_a(0)=1,\qquad P_a(s+1)=(1-aQ^{s+1})P_a(s),\\
 P_a(j)=(Qa;Q)_j,\qquad
 P_a(s+N)=(1-a^Ne^{2\pi is})P_a(s).
 \end{gathered}
 \tag{10}
\]
Every branch in these formulas is fixed by the displayed disk
logarithms. We do not identify \(P_a\) with a ratio of shifted
canonical factorials; a periodic factor between two possible
interpolations is not being discarded.

Put \(s=Nu-1/2\), and define the normalized wall interpolation
\[
 W_N(u;y,z)=\frac{\kappa}{\sqrt N}F_N(s)
       \frac{P_{yz}(s)}
            {P_{-q^{-1}y}(s+1)P_{-q^{-1}z}(s+1)} .
 \tag{11}
\]
Equation (10) proves that it has exactly the values in (3).
For \(E=e^{2\pi iNu}=-e^{2\pi is}\), its one-turn multiplier is
\[
 \begin{aligned}
 W_N(u+1)&=M_N(u)W_N(u),\\
 M_N(u)&=\frac{(1+E)(1+(yz)^NE)}
                  {(1+\eta y^NE)(1+\eta z^NE)},\\
 M_N(u)-1&=
       \frac{E D_N(y)D_N(z)}
                  {(1+\eta y^NE)(1+\eta z^NE)} .
 \end{aligned}
 \tag{12}
\]
Thus the source's missing cyclic arrow is retained explicitly.

## 2. A global argument bound for the source characteristic

Use the initialized action from the wall theorem,
\[
 \Psi(x,y,z)=-\frac{\pi}{12}
  +\frac{\operatorname{Li}_2(-x)+\operatorname{Li}_2(-y)
       +\operatorname{Li}_2(-z)+\operatorname{Li}_2(-xyz)
       -\operatorname{Li}_2(xy)-\operatorname{Li}_2(xz)
       -\operatorname{Li}_2(yz)}{2\pi},
\]
with its disk power-series branches, and put
\[
 R_x(x,y,z)=\frac{(1-xy)(1-xz)}
                       {(1+x)(1+xyz)}.
 \tag{13}
\]
For every \((x,y,z)\in\mathbb D^3\), this ratio avoids the
nonpositive real axis. Here is a direct proof.

Fix \(y,z\), put \(c=yz\), \(A=(1+y)(1+z)\), and write
\[
 R_x=1-Af(x),\qquad f(x)=\frac{x}{(1+x)(1+cx)}.
 \tag{14}
\]
Equality \(f(x_1)=f(x_2)\) factors as
\((x_1-x_2)(1-cx_1x_2)=0\), so \(f\) is univalent on the disk.
Moreover
\[
 \operatorname{Re}\frac{x f'(x)}{f(x)}
 =\operatorname{Re}\left\{\frac1{1+x}+\frac1{1+cx}-1\right\}>0.
 \tag{15}
\]
The argument of \(f(re^{i\theta})\) therefore increases strictly
around each circle. Its image encloses zero once and meets every
ray once, so \(f(\mathbb D)\) is starlike about zero.
It follows that \(R_x(\mathbb D)\) is starlike about one.
But \(R_x\) has no zero in the disk. Its image cannot contain a
nonpositive real number, since the segment from one to that number
would contain zero. This proves the assertion.

The logarithm anchored at \(x=0\) is consequently the principal
one, and
\[
 2\pi x\partial_x\Psi=\Log R_x,\qquad
                              |\operatorname{Im}\Log R_x|<\pi.
 \tag{16}
\]
Direct substitution in the dilogarithm expression gives
\(\Psi(-1,y,z)=0\) as a boundary value: the nonconstant terms
cancel, and \(\operatorname{Li}_2(1)/(2\pi)=\pi/12\).
On \(x=-e^{-2\pi v}\), differentiation of (16) therefore yields
\[
 h(v):=\operatorname{Re}\{i\Psi(-e^{-2\pi v},y,z)\},\qquad
 h(0)=0,\quad h'(v)=\operatorname{Im}\Log R_x.
\]
In particular
\[
                              |h(v)|\le\pi v\qquad(v\ge0).
 \tag{17}
\]

## 3. The actual interpolation on the upper cut

The literal half-step admits an exact factorial modulus.
For \(Y\ge0\), equations (5) imply
\[
 |G_N(-1/2+iY)|^2=\frac{N}{2\cosh(\pi Y)}.
 \tag{18}
\]
Indeed the product of \(N\) sine shifts at
\(s=-1/2+iY\) is \(2\cosh(\pi Y)\). Reflection and reality give
\(G_N(s+N)=N/\overline{G_N(s)}\), proving (18).
The quadratic Gaussian in (6) has unit modulus at this half-step,
whereas \(|e^{-\pi is/2}|^2=e^{\pi Y}\). Hence
\[
 \boxed{\qquad
 |F_N(-1/2+iY)|^2=\frac{N}{1+e^{-2\pi Y}}\le N.
 \qquad}
 \tag{19}
\]
This concerns precisely \(s=Nu-1/2\) at \(u=iv\); it is not an
estimate on a differently shifted cut.

We also need uniform control of the regular factors, for all
\(v\ge0\). For \(|a|\le\rho<1\), \(|z|\le1\), finite Fourier
summation in (8) and the low-frequency expansion give
\[
 \log\mathcal E_a(z)
  =\frac{iN}{2\pi}\operatorname{Li}_2(az)
                     +\frac12\Log(1-az)+O_\rho(N^{-1}).
 \tag{20}
\]
For clarity, at frequencies not divisible by \(N\) its coefficient
is \(Q^n/[n(1-Q^n)]\); for \(n\le N/2\),
\[
 \frac{Q^n}{1-Q^n}=-\frac{N}{2\pi in}-\frac12+O(n/N).
\]
The remaining frequencies have exponentially small disk tails
using \(|1-Q^n|\ge c\min(n,N-n)/N\), with residues modulo \(N\)
for higher frequencies. The multiples of \(N\) contribute
\((d/(2N))\Log(1-(az)^N)=O_\rho(\rho^N)\).
These bounds prove (20) uniformly on the indicated closed sets.

At \(s=-1/2+iNv\), the extra logarithm in (8) is bounded by
\[
 C_\rho(v+1/N)\rho^N e^{-2\pi Nv}=O_\rho(\rho^N/N).
 \tag{21}
\]
The same holds for \(s+1\). Expanding the \(q^{-1}\) half-shifts
in (20) now gives, uniformly for every \(v\ge0\),
\[
 \frac{P_{yz}(s)}
      {P_{-q^{-1}y}(s+1)P_{-q^{-1}z}(s+1)}
   =B(-w,y,z)
     e^{N\{I_{yz}(iv)-I_{-y}(iv)-I_{-z}(iv)\}}
                                      (1+O_\rho(N^{-1})),
 \quad w=e^{-2\pi v},
 \tag{22}
\]
where
\[
 I_a(u)=-\frac{\operatorname{Li}_2(ae^{2\pi iu})
                    -\operatorname{Li}_2(a)}{2\pi i},\qquad
 B(x,y,z)=[(1-xy)(1-xz)(1-yz)]^{-1/2}.
\]
All roots and logarithms are anchored in the disk.
The exponent in braces is
\(i\Psi(-w,y,z)-i\Psi(-w,0,0)\).
The second term is purely imaginary for \(0\le w\le1\), so its
real part is exactly \(h(v)\).
Also \(B(-w,y,z)\) is uniformly bounded and bounded away from zero.
Combining (11), (19), and (22) gives the actual source bound
\[
                         |W_N(iv;y,z)|\le C_\rho e^{Nh(v)}.
 \tag{23}
\]
The factor \(\sqrt N\) in (19) cancels the original \(1/\sqrt N\)
in (11). Using (12) and (17), with \(|y|,|z|\le\rho\), proves
\[
 \boxed{\qquad
 |(M_N(iv)-1)W_N(iv;y,z)|\le C_\rho e^{-\pi Nv}
                                                   \quad(v\ge0).
 \qquad}
 \tag{24}
\]
This is an estimate for the whole upper-cut jump of the chosen
source interpolation, not just for its value at a prospective pole.

## 4. The complete contour identity, with the lower term retained

Let \(x\in\mathbb D\setminus(-1,0]\), and choose the unique
\(u_x\) with \(0<\operatorname{Re}u_x<1\),
\(\operatorname{Im}u_x>0\), and \(-e^{2\pi iu_x}=x\).
For fixed \(\rho<1\), choose
\[
                   0<b<-\frac{\log\rho}{2\pi}.
\]
The interpolation (11) is holomorphic on the rectangle
\(0\le\operatorname{Re}u\le1\), \(-b\le\operatorname{Im}u\le Y\):
the canonical factorial stays in its original real-part strip,
and every regular factor in (8) has argument of modulus below one.
Define
\[
 K_N(u)=\frac{-2\pi i}{1+e^{2\pi iNu}},\qquad
 \mathcal I_N(u)=
                  \frac{K_N(u)W_N(u;y,z)}{1+x e^{-2\pi iu}}.
 \tag{25}
\]
At \(u_j\), \(K_N\) has residue \(1/N\). At \(u_x\),
\(\mathcal I_N\) has residue
\(-W_N(u_x)/D_N(x)\), since \(1+e^{2\pi iNu_x}=D_N(x)\).
There are no other poles in this rectangle when \(Y>\operatorname{Im}u_x\).
The residue theorem and (4) therefore apply with the complete
finite support, without a periodic interpolation of its last arrow.

The upper horizontal integral tends to zero as \(Y\to\infty\),
for each fixed \(N\). Here the exact finite cotangent formula for
\(G_N'/G_N\) shows that the Gaussian-corrected \(F_N(s)\)
is bounded as \(\operatorname{Im}s\to+\infty\) in this fixed
real-part strip: its linear leading logarithmic derivatives cancel,
leaving \(O_N((1+|s|)e^{-2\pi\operatorname{Im}s/N})\).
The regular factors tend to finite constants, whereas the Cauchy
denominator grows like \(e^{2\pi Y}\). No uniform-in-\(N\) bound
is needed before taking this exact fixed-\(N\) contour limit.

Since \(\mathcal I_N(u+1)=M_N(u)\mathcal I_N(u)\), the resulting
identity is
\[
 \boxed{\quad
 \widehat{\mathcal C}_N
    =\frac{W_N(u_x)}{D_N(x)}+\mathcal L_{N,b}+\mathcal U_N,
 \quad}
 \tag{26}
\]
where all orientations are explicit:
\[
 \begin{aligned}
 \mathcal L_{N,b}
   &={1\over2\pi i}\int_{-ib}^{1-ib}\mathcal I_N(u)\,du
     +{1\over2\pi}\int_{-b}^{0}
                 (M_N(iv)-1)\mathcal I_N(iv)\,dv,\\
 \mathcal U_N
   &={1\over2\pi}\int_0^\infty
                 (M_N(iv)-1)\mathcal I_N(iv)\,dv .
 \end{aligned}
 \tag{27}
\]
The two vertical sides have been combined using their exact
one-turn multiplier, not suppressed separately. The lower contour
\(\mathcal L_{N,b}\) is retained; no asymptotic bound for it is asserted.

For \(0<\delta<\pi\), assume \(|\arg x|\le\pi-\delta\).
Then
\[
 |1+x e^{2\pi v}|
        \ge\sin(\delta/2)(1+|x|e^{2\pi v}),\qquad
 |K_N(iv)|\le2\pi.
\]
Equation (24) and integration in \(v\) give
\[
 \boxed{\qquad
             |\mathcal U_N|\le
                   \frac{C_\rho}{N\sin(\delta/2)} .
 \qquad}
 \tag{28}
\]
There is no sampling pole at \(v=0\): \(e^{2\pi iN\cdot0}=1\)
and the kernel's denominator is two. Thus the ordinary integral
in (27) needs no endpoint finite-part convention.

Multiplying (26) by \(D_N(x)D_N(y)D_N(z)\) recovers the original
polynomial source with all norm factors retained. On a strictly
growing geometric family, (28) is subexponential and hence smaller
than its nonzero candidate exponential pole packet. The same
comparison has not been proved for \(\mathcal L_{N,b}\).
Consequently (26)--(28) do not prove full radial transport or a
volume lower bound after general Conway gluing.

## Complete proof sources

All three complete proof sources were read at their matching pins:

| Source | SHA-256 |
|---|---|
| [Exact wall values and Cauchy source](research_centered_tensor_wall_cauchy_source.md) | 3cda6a170c46abf27a1c8c15b110780ebcb6017a5aa18758a4e51ba0a271892c |
| [Canonical factorial and original contour](exact_factorial_interpolation_and_complex_contours.md) | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| [Finite derivative of the canonical factorial](research_exact_cyclotomic_factorial.md) | 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b |

The regular cochains and the global principal-argument estimate are
proved above. Their purpose is the explicit upper-cut bound for an
exact representation of the prescribed finite source. No equivalence
of different off-lattice interpolation gauges is assumed. No novelty
is claimed for reflection, finite product cochains, or the residue theorem.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
