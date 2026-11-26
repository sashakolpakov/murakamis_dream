# Exponential cancellation of the actual low and central high endpoint bands

Private written proof, 16 November 2026.

The low endpoint polynomial and the central portion of its original
high Newton band cancel exponentially after division by the
distinct-node polynomial, on fixed lower angular compact sets. This
holds at both level parities. It follows from the exact original
kernel difference equation and a holomorphic iteration with a fixed
domain buffer. No formal asymptotic series is used to infer the
exponential error.

The result combines the actual low term with the half-character term
before estimating them. It extends to arbitrary fixed products of
endpoint coupons at a shared surviving vertex. It does not discard
the vertical sides or the remaining physical rows. The positive
exponential constant obtained here is not compared with a filled
action deficit, and no full-source asymptotic or nonzero cycle
coefficient follows.

## 1. Exact original polynomials and the general central band

Put
\[
 N\ge2,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 k_0=N-m,\quad J=k_0-1,\quad \theta=\pi/N,\quad\eta=(-1)^D,
\]
\[
 c_a=2\cos((2a+1)\theta),\quad s_j=2\sin(j\theta),\quad
 S_j=\prod_{b=1}^j s_b,\qquad
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),
\]
\[
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z),\qquad
 Z(t)=-2\cos t,\qquad w_N(\alpha)=2\cosh(\alpha/N).
 \tag{1}
\]
The monic polynomial of distinct physical nodes is
\[
 Q_N(Z)=
 \begin{cases}
 2T_m(Z/2),&N=2m,\\
 (Z+2)\{U_m(Z/2)-U_{m-1}(Z/2)\},&N=2m+1.
 \end{cases}                                               \tag{2}
\]
Its degree is \(k_0=J+1\). In angular coordinates,
\[
 Q_N(Z(t))=
 \begin{cases}
 2(-1)^m\cos(Nt/2),&N=2m,\\
 4(-1)^m\sin(t/2)\sin(Nt/2),&N=2m+1.
 \end{cases}                                               \tag{3}
\]
All of these are ordinary polynomial identities.
The original closing, used below, is
\[
 \phi_N(h)=\eta\sum_{a<m}
     \{(4-c_a^2)h'(c_a)-c_ah(c_a)\}
                 +\mathbf1_{N\ {\rm odd}}h(-2).
 \tag{3a}
\]

Fix \(0<\delta<1/2\), put \(L_N=\lfloor\delta N\rfloor\), and
take \(N\) sufficiently large that
\(k_*:=k_0+L_N\le D\). Define
\[
 \begin{split}
 \mathcal L_N(\alpha,Z)&=\sum_{j=0}^{J}e_j(w_N(\alpha))e_j(Z),\\
 \mathcal P_N^\delta(\alpha,Z)
     &=\sum_{j=0}^{k_*}e_j(w_N(\alpha))e_j(Z),\\
 \mathcal E_N^\delta(\alpha,t)
     &=\frac{\mathcal P_N^\delta(\alpha,Z(t))}{Q_N(Z(t))}.
 \end{split}                                               \tag{4}
\]
The notation \(\mathcal P_N^\delta\) is a partial kernel, not the
physical relation \(P_N(Z)=2T_N(Z/2)+2\). The low polynomial
\(\mathcal L_N\) has degree at most \(J\).

Use the general-domain source's exact ratios
\[
 (a_l,b_l)=
 \begin{cases}
 ((l+\tfrac12)\theta,(l+1)\theta),&N=2m,\\
 ((l+1)\theta,(l+\tfrac32)\theta),&N=2m+1,
 \end{cases}
\]
\[
 \rho_{l,N}(\alpha,t)=
 \frac{[\cos^2a_l+\sinh^2(\alpha/(2N))]
       [\sin^2(t/2)-\sin^2a_l]}{\cos^4b_l},
 \qquad
 H_N^\delta=\sum_{l=0}^{L_N}\prod_{j<l}\rho_{j,N}.           \tag{5}
\]
An empty product is one. Direct Newton multiplication gives
\[
 \frac{e_{k_0+l}(w_N(\alpha))e_{k_0+l}(Z(t))}
      {Q_N(Z(t))}
       =\beta_N(\alpha)\prod_{j<l}\rho_{j,N}(\alpha,t),       \tag{6}
\]
where
\[
 \beta_N(\alpha)=
 \begin{cases}
 \displaystyle\frac{\cosh(\alpha/2)}{2N^2},&N=2m,\\[4pt]
 \displaystyle
 \frac{\cosh(\alpha/2)\cosh(\alpha/(2N))}
             {4N^2\cos^4(\theta/2)},&N=2m+1.
 \end{cases}                                               \tag{7}
\]
For clarity, at \(l=0\) one uses
\[
 e_{k_0}(Z)/Q_N(Z)=(-1)^{k_0}/S_{k_0}^2,
\quad
 S_{k_0}^2=
 \begin{cases}2N,&N\ {\rm even},\\4N\cos^2(\theta/2),&N\ {\rm odd},
 \end{cases}
\]
and the exact endpoint value given by the sine products.
Equivalently, evaluate (2) directly at \(w_N(\alpha)\):
its values are \(2\cosh(\alpha/2)\) at even levels and
\(4\cosh(\alpha/2)\cosh(\alpha/(2N))\) at odd levels.
Together with the displayed \(S_{k_0}^2\), this gives (7).
The ratio of the left side of (6) at \(l+1\) to that at \(l\) is
\[
       \frac{(c_{k_0+l}-w_N(\alpha))(c_{k_0+l}-Z(t))}
                         {s_{k_0+l+1}^{\,4}},
                                                               \tag{8}
\]
which is precisely (5). This proves (6) without identifying
polynomials from values alone. In particular,
\[
       \mathcal E_N^\delta
          =\frac{\mathcal L_N}{Q_N}+\beta_NH_N^\delta.       \tag{9}
\]

The fixed contraction domain is
\[
 \mathcal D_\delta
 =\{t:|\sin^2(t/2)-\sin^2(\pi\delta)|<\cos^2(\pi\delta)\}.
                                                               \tag{10}
\]
The general-domain theorem proves that on each compact subset of
\(\mathcal D_\delta\), uniformly for bounded complex \(\alpha\),
there are \(q<1\) and \(N_0\) such that
\[
                    |\rho_{l,N}|\le q\quad(0\le l<L_N).
                                                               \tag{11}
\]
The upper bound on complex \(\alpha\) in the theorem below is
stronger, \(|\alpha|<\pi\), because its a priori low-polynomial
bound uses the endpoint root disk.

## 2. An a priori bound with no low/high cancellation assumed

Fix \(A<\pi\). For \(|\alpha|\le A\), the endpoint root theorem
gives, for every distinct physical node and all sufficiently large \(N\),
\[
 |K_N(w_N(\alpha),c_a)|\le1.                               \tag{12}
\]
Indeed
\[
 |w_N(\alpha)-2|\le2(\cosh(A/N)-1)\le2-c_0
 \]
eventually, since \(A<\pi\). This is a complex disk estimate, not a
positivity assertion for complex endpoint colors.

The high Newton terms vanish at every distinct node. Thus ordinary
Lagrange interpolation gives the exact partial fractions
\[
 \frac{\mathcal L_N(\alpha,Z)}{Q_N(Z)}
 =\sum_{\text{distinct }a}
       \frac{K_N(w_N(\alpha),c_a)}
                    {Q_N'(c_a)(Z-c_a)}.                   \tag{13}
\]
The reciprocal derivative weights satisfy
\[
 |Q_N'(c_a)|^{-1}=
 \begin{cases}
 2\sin\tau_a/N,&N\ {\rm even},\\
 2\cos(\tau_a/2)/N,&N\ {\rm odd},\ a<m,\\
 1/N,&N\ {\rm odd},\ c_a=-2,
 \end{cases}
\quad
 \tau_a=\pi(D-2a)/N.                                      \tag{14}
\]
These follow by differentiating (3); the last follows at its
ramified angular zero or directly from the polynomial in (2).
Their sum is at most one. Hence, for \(Z\notin[-2,2]\),
\[
          \left|\frac{\mathcal L_N(\alpha,Z)}{Q_N(Z)}\right|
                 \le\frac1{\operatorname{dist}(Z,[-2,2])}.
                                                               \tag{15}
\]
This retains the odd simple node.

Let
\[
                  \mathcal U_\delta
                    =\mathcal D_\delta\cap\{\Im t<0\}.
                                                               \tag{16}
\]
For every compact \(\mathcal K_0\Subset\mathcal U_\delta\),
\(Z(\mathcal K_0)\) has positive distance from \([-2,2]\).
Equations (7), (9), (11), and (15) therefore give
\[
       \sup_{|\alpha|\le A,\ t\in\mathcal K_0}
                        |\mathcal E_N^\delta(\alpha,t)|\le C.
                                                               \tag{17}
\]
No asymptotic of the Cauchy transform in (13), nor any cancellation
between the two terms in (9), is used in (17).

## 3. The exact gauged difference equation

Define the original angular difference coefficients
\[
 A_N(t)=\frac{4\cos^4((t-\theta)/2)}
                    {\sin t\,\sin(t-\theta)},\qquad
 C_N(t)=\frac{4\cos^4((t+\theta)/2)}
                    {\sin t\,\sin(t+\theta)}.
                                                               \tag{18}
\]
The full kernel difference source, after the substitution
\(x=(\pi-t-\theta)/(2\theta)\) in its physical-color index, gives
\[
 (\mathscr L_N f)(t)
  =(c_0+A_N+C_N)f(t)-A_Nf(t-2\theta)-C_Nf(t+2\theta),
\]
\[
             \mathscr L_N e_j=c_je_j-s_j^2e_{j-1}.
                                                               \tag{19}
\]
The \(j=0\) lowering term is zero. The multiplication identity
\(w e_j(w)=c_je_j(w)-s_{j+1}^2e_{j+1}(w)\) consequently telescopes:
\[
 (\mathscr L_N-w_N)\mathcal P_N^\delta
       =s_{k_*+1}^2e_{k_*+1}(w_N)e_{k_*}(Z).
                                                               \tag{20}
\]
We use (20) only for sufficiently large \(N\), when \(k_*<D\);
this holds for the fixed \(\delta<1/2\). It is an ordinary
polynomial identity, including every physical normal.

The exact shift ratios of \(Q_N\) are
\[
 \frac{Q_N(Z(t\pm2\theta))}{Q_N(Z(t))}
  =\begin{cases}
       -1,&N\ {\rm even},\\
       -\sin(t/2\pm\theta)/\sin(t/2),&N\ {\rm odd}.
    \end{cases}                                           \tag{21}
\]
Set \(\widetilde A_N=A_N,\widetilde C_N=C_N\) in the even case;
in the odd case set
\[
 \widetilde A_N=A_N\frac{\sin(t/2-\theta)}{\sin(t/2)},\qquad
 \widetilde C_N=C_N\frac{\sin(t/2+\theta)}{\sin(t/2)}.
\]
Then (20), divided by \(Q_N\), becomes
\[
 M_N\mathcal E_N^\delta
 +\widetilde A_N\{\mathcal E_N^\delta(t-2\theta)-\mathcal E_N^\delta(t)\}
 +\widetilde C_N\{\mathcal E_N^\delta(t+2\theta)-\mathcal E_N^\delta(t)\}
       =\mathcal F_N,                                     \tag{22}
\]
where
\[
 \begin{split}
 M_N&=c_0-w_N+A_N+C_N+\widetilde A_N+\widetilde C_N,\\
 \mathcal F_N
   &=(c_{k_*}-w_N)\beta_N
                         \prod_{l=0}^{L_N-1}\rho_{l,N}.
 \end{split}                                               \tag{23}
\]
The last formula follows from (6) and
\(s_{k_*+1}^2e_{k_*+1}(w_N)=(c_{k_*}-w_N)e_{k_*}(w_N)\).
Thus on every fixed compact in (16),
\[
                    |\mathcal F_N|\le CN^{-2}q^{L_N}.      \tag{24}
\]
There is no undetermined homogeneous error in (22).

All its coefficients are holomorphic on fixed lower neighborhoods
for large \(N\). Uniformly on them and on \(|\alpha|\le A\),
\[
 A_N,\ C_N,\ \widetilde A_N,\ \widetilde C_N
                 \longrightarrow \cot^2(t/2),\qquad
                  M_N\longrightarrow4\cot^2(t/2).          \tag{25}
\]
The limiting multiplier is nonzero off the real axis.
In particular \(M_N^{-1}\) is uniformly bounded on the neighborhoods
used below. No positivity of this complex multiplier is assumed.

## 4. Exponential cancellation by holomorphic iteration

**Theorem 1.** For every \(0<\delta<1/2\), every \(A<\pi\), and
every compact \(\mathcal K\Subset\mathcal U_\delta\), there are
\(C,\kappa>0\) and \(N_0\) such that, at both level parities,
\[
 \boxed{\qquad
 \sup_{|\alpha|\le A,\ t\in\mathcal K}
       \left|\frac{\mathcal P_N^\delta(\alpha,Z(t))}
                         {Q_N(Z(t))}\right|
                         \le C e^{-\kappa N}
                  \qquad(N\ge N_0).
 \qquad}                                                   \tag{26}
\]
All fixed derivatives in \(\alpha,t\) have the same form of bound
on smaller compact sets. In the endpoint spectral color, for fixed
nonnegative integers \(a,b\),
\[
 \left|\partial_w^a\partial_Z^b
       \frac{\sum_{j=0}^{k_*}e_j(w)e_j(Z)}{Q_N(Z)}
       \right|_{\substack{w=w_N(\alpha)\\Z=Z(t)}}
            \le C_{a,b}N^{2a}e^{-\kappa N}                 \tag{27}
\]
on compact parameter sets as above, after choosing a larger
parameter/domain neighborhood for the proof. These are derivatives
of the displayed quotient, not of its numerator alone.

**Proof.** Choose a larger \(\alpha\)-disk still of radius less
than \(\pi\). Choose \(\rho>0\) such that the closed \(3\rho\)
neighborhood of \(\mathcal K\) lies in \(\mathcal U_\delta\).
On that neighborhood use (11), (17), and (25), and put
\[
 B=\sup\frac{|\widetilde A_N|+|\widetilde C_N|}{|M_N|}<\infty,
 \qquad
 G_N=M_N^{-1}\mathcal F_N,
\]
\[
 (\mathscr P_N f)(t)=
 -M_N^{-1}\{\widetilde A_N(f(t-2\theta)-f(t))
                +\widetilde C_N(f(t+2\theta)-f(t))\}.
                                                               \tag{28}
\]
The bounds are uniform for all sufficiently large \(N\) and all
parameters in the chosen disk. Equation (22) is exactly
\(\mathcal E_N^\delta=G_N+\mathscr P_N\mathcal E_N^\delta\).

Here is the domain estimate needed for an increasing number of
iterations. If two nested tubular neighborhoods have gap \(d\)
and \(d\ge4\theta\), Cauchy's inequality on the outer neighborhood
and integration along the real shift segment give
\[
       \|\mathscr P_N f\|_{\rm inner}
             \le \frac{4\theta B}{d}\|f\|_{\rm outer}.
                                                               \tag{29}
\]
The intermediate segment remains at distance at least \(d/2\)
from the outer boundary. This proves (29) without a derivative
bound on \(f\) assumed in advance.

Choose a fixed \(a_*>0\) so small that
\[
 a_*\le\frac{\rho}{16\pi\max(1,B)},\qquad a_*\le\frac14,
 \]
and put \(k_N=\lfloor a_*N\rfloor\).
Use \(k_N\) successive gaps \(d=\rho/k_N\), from the \(2\rho\)
neighborhood to the \(\rho\) neighborhood. Then \(d\ge4\theta\)
and the norm in (29) is at most \(1/2\). Repeated substitution
in the exact equation gives
\[
 \mathcal E_N^\delta
     =\sum_{j=0}^{k_N-1}\mathscr P_N^{\,j}G_N
                          +\mathscr P_N^{\,k_N}\mathcal E_N^\delta.
                                                               \tag{30}
\]
Each composition is taken between the indicated nested domains.
Consequently
\[
 \|\mathcal E_N^\delta\|_{\rho}
       \le2\|G_N\|_{2\rho}
                         +2^{-k_N}\|\mathcal E_N^\delta\|_{2\rho}
       \le C N^{-2}q^{L_N}+C2^{-k_N}.                     \tag{31}
\]
Since \(L_N\ge\delta N/2\) and \(k_N\ge a_*N/2\) for large \(N\),
one may, for example, take
\[
 \kappa=\min\left\{\frac{\delta}{2}\log\frac1q,\
                                \frac{a_*}{2}\log2\right\}>0.
                                                               \tag{32}
\]
This proves (26). It is an estimate for an actual finite function,
not optimal truncation of a formal series.

The unused domain buffer and Cauchy's formula give fixed angular
and parameter derivatives. Since \(dZ/dt=2\sin t\) is nonzero
on the lower compact, spectral \(Z\)-derivatives follow there too.
The function is even in \(\alpha\), so it descends holomorphically
to \(u=\alpha^2\). On bounded \(u\)-disks,
\[
             N^2(w_N(\alpha)-2)=u+O(N^{-2})
 \]
with all fixed derivatives, and this map has a uniformly regular
inverse on slightly smaller disks for large \(N\).
Thus each endpoint derivative costs at most \(C_aN^{2a}\);
this includes \(\alpha=0\). It proves (27).
\(\square\)

For example, the entire rectangle
\(|\Re t|\le\pi/4,\ |\Im t|\le\log3\) lies compactly in
\(\mathcal D_{1/8}\), by the general-domain theorem.
Every fixed closed lower subrectangle with \(\Im t\le-h_0<0\)
therefore satisfies (26). The constants depend on its buffer,
on \(\delta\), and on the parameter disk. No universal action gap
is claimed from their positivity.

## 5. Exact cancellation in the half-charge horizontal density

Let \(\Gamma_N^\delta\) be the actual high-character amplitude in
the general-domain source. Equations (5)--(9) give exactly
\[
 \Gamma_N^\delta+
       2N\sin t\,\frac{\mathcal L_N}{Q_N}
        =2N\sin t\,\mathcal E_N^\delta
                                      \quad(N\ {\rm even}),
\]
\[
 \Gamma_N^\delta+
       4N\sin t\sin(t/2)\,\frac{\mathcal L_N}{Q_N}
        =4N\sin t\sin(t/2)\,\mathcal E_N^\delta
                                      \quad(N\ {\rm odd}).
                                                               \tag{33}
\]
Thus the actual low term cancels the central high amplitude to
exponential accuracy on the domains of Theorem 1. The separate
leading profiles of these two terms are not whole-source
coefficients.

To see the original contour normalization directly, set
\(\zeta=e^{-iNt}\), and keep the original Gaussian carrier
\[
 \mathfrak c_{N,n}=e^{\pi i nD^2/(4N)},\qquad
                  G_n(t)=e^{inNt^2/(4\pi)}.
 \]
For a unit-charge central rectangle with grid-midpoint end \(b_N\),
the low horizontal coefficient is \(-N^2\mathfrak c_{N,n}/(\pi i)\)
with kernel \(\zeta/(1-\eta\zeta)^2\). The exact high horizontal
coefficient is \(N i^{-D}\mathfrak c_{N,n}/(2\pi)\) with kernel
\(\zeta^{1/2}/(1-\eta\zeta)\). Here \(\zeta^{1/2}\) means the
specified entire character \(e^{-iNt/2}\). Their common amplitude is
\[
 \Gamma_N^\delta+
   2i^{D+1}N\sin t\,\mathcal L_N
                         \frac{\zeta^{1/2}}{1-\eta\zeta}.
                                                               \tag{34}
\]
Substituting (3) into (34) gives precisely (33).
Every horizontal alias is retained in these identities.
The original low and high vertical integrals remain; they have
not been assigned the lower-compact estimate (26) at height zero.

## 6. Shared coupons and the exact retained central trace

The preceding cancellation takes place before evaluating any
spectator. It can be used for an arbitrary fixed number \(r\ge1\)
of endpoint coupons at one original traced vertex, with bounded
parameters \(|\alpha_i|<\pi\).

First, the omitted polynomial
\[
 \mathcal O_N^\delta(\alpha,Z)
     =K_N(w_N(\alpha),Z)-\mathcal P_N^\delta(\alpha,Z)
 \]
is a sum of the original high modes with
\(j\ge k_0+L_N+1\). Its physical values all vanish. Its first
normal can occur only at nodes with
\[
 \tau_a\ge
 \begin{cases}
 (2L_N+3)\theta,&N\ {\rm even},\\
 (2L_N+4)\theta,&N\ {\rm odd}.
 \end{cases}                                               \tag{35}
\]
Indeed put \(j=D-r'\). The full-high contraction has normal
support \(a\le r'\): in the defining Newton product the two
occurrences of \(c_a\) have indices \(a\) and \(D-a\), so the
derivative vanishes once \(j>D-a\). Here \(r'\le m-2-L_N\); substituting
the largest allowed \(a\) into \(\tau_a=(D-2a)\theta\) gives (35).
The odd simple value is also zero.

The omitted band is therefore the following exact value functional,
with its original normal weights:
\[
 \phi_N(\mathcal O_N^\delta f)
   =\eta\sum_{a=0}^{m-2-L_N}
          (4-c_a^2)(\mathcal O_N^\delta)'(c_a)f(c_a).
 \tag{35a}
\]
For several coupons, write \(B_i=K_N(w_N(\alpha_i),\cdot)\),
\(P_i=\mathcal P_N^\delta(\alpha_i,\cdot)\), and \(O_i=B_i-P_i\).
Every \(O_i\) vanishes at all physical nodes, so the product of two
of them has zero values and first normals. Consequently
\[
 \begin{split}
 \phi_N\!\left[\left(\prod_iB_i-\prod_iP_i\right)f\right]
    &=\sum_{a=0}^{m-2-L_N}\omega_a f(c_a),\\
 \omega_a&=\eta(4-c_a^2)
        \sum_i O_i'(c_a)\prod_{j\ne i}B_j(c_a).
 \end{split}                                               \tag{35b}
\]
Each shared physical color in (35b) is kept, together with the
entire remaining spectator. These identities do not give a
filled-action estimate for that physical sum.

Consequently, for every fixed \(b<2\pi\delta\) and all large \(N\),
the full values and first normals of
\[
        \prod_{i=1}^rK_N(w_N(\alpha_i),Z)
 \quad\hbox{and}\quad
        \prod_{i=1}^r\mathcal P_N^\delta(\alpha_i,Z)
                                                               \tag{36}
\]
agree at every physical node with \(|t|\le b\), including the odd
simple node. This follows by the product rule, not from a
value-only replacement. Thus (36) can be made inside the original
central trace with any shared polynomial spectator, retaining
all other traces coefficientwise.

Here is the full contour statement. Let \(b_N\le b<2\pi\delta\)
be a positive midpoint, \(e^{iNb_N}=-\eta\), and let \(H>0\).
Let \(f(Z(t))\) be even and holomorphic near the closed rectangle
\([-b_N,b_N]+i[-H,H]\). Write
\[
 p_N(t)=\prod_{i=1}^r\mathcal P_N^\delta(\alpha_i,Z(t)),
 \quad
 g_N(t)=\sin t\,p_N(t)f(Z(t))G_n(t).
 \]
The original central full-normal trace, at unit charge, is exactly
\[
 -\frac{N^2\mathfrak c_{N,n}}{\pi i}
    \int_{-b_N-iH}^{b_N-iH}
          g_N(t)\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt
 +\frac{\eta N^2\mathfrak c_{N,n}}{\pi}
    \int_{-H}^{H}\frac{g_N(b_N+ih)}{4\cosh^2(Nh/2)}\,dh .
                                                               \tag{37}
\]
The source derivative-sampling residue proof applies on this
midpoint rectangle exactly as on the full-period rectangle.
At each double node the two angular copies give its value and
first normal; at the odd zero angle the derivative sampling gives
the original simple value. The replacement (36) therefore changes
neither contribution. The second integral and the actual midpoint
orientation are part of (37).

Define
\[
 \xi_N(t)=
 \begin{cases}
 (-1)^m,&N\ {\rm even},\\
 -2i(-1)^m\sin(t/2),&N\ {\rm odd}.
 \end{cases}
 \]
Equation (3) is
\(Q_N(Z(t))=\xi_N(t)e^{iNt/2}(1-\eta e^{-iNt})\).
The horizontal density in (37) consequently becomes exactly
\[
 \sin t\,\xi_N(t)^r f(Z(t))G_n(t)
       \left(\prod_{i=1}^r\mathcal E_N^\delta(\alpha_i,t)\right)
       e^{-iN(1-r/2)t}(1-\eta e^{-iNt})^{r-2}.              \tag{38}
\]
All shared variables remain in \(f\). On a fixed lower compact
contained in \(\mathcal U_\delta\), the product of quotients in
(38) is \(O(e^{-r\kappa N})\), with its fixed derivatives.
For fixed \(H>0\) and a family of lower segments in such a compact,
the horizontal integral in (37) is therefore bounded by
\[
 C_r N^2|\mathfrak c_{N,n}|e^{-r\kappa N}
       \int_{-b_N-iH}^{b_N-iH}
                |f(Z(t))G_n(t)e^{-iN(1-r/2)t}|\,|dt|.
                                                               \tag{39}
\]
The remaining factors in (38) are uniformly bounded there, including
the inverse factor when \(r=1\). Formula (39) is an actual relative
gain in the coherent horizontal density with the spectator retained.
Its charge character and its spectator are not replaced by a
claimed filled-action estimate.

The full physical trace is the central trace (37) plus the literal
sum of its remaining physical rows. No row outside the window in
(35), or vertical term in (37), is discarded. The theorem gives
no bound for those terms at the filled rate. It also does not assert
that (39)'s \(\kappa\) exceeds any independently arising action loss.

## 7. Direct-source readback

The following complete direct sources were read, their used
identities checked, and their hashes verified:

* [Original kernel difference equation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_edge_kernel_difference_and_endpoint_bound.md),
  SHA256 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da:
  original lowering operator, physical angular conversion and the
  ordinary finite-kernel defect. Its weaker root bound is not used.
* [Coherent endpoint kernel reduction](research_full_period_endpoint_kernel_reduction.md),
  SHA256 a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e:
  the stronger physical-row root disk, exact low interpolation and
  both-parity full-normal trace conventions.
* [General endpoint half-character domain](research_endpoint_radical_general_domain.md),
  SHA256 600ae0d78f29946272ed54b600cb1f5fdf170965985a08d6e3d9201303722074:
  exact lowering ratios, general-cutoff contraction domain, original
  character amplitude and midpoint contour with its vertical term.
* [Full-period current and charge convolution](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595:
  original Gaussian carrier, derivative sampling, full-normal
  rectangle orientation, and coefficientwise spectator convention.

Only written mathematics, text reads and hashes were used. No
mathematical program, numerical experiment, test or compilation was
run. Frozen notes and public manuscripts are unchanged.
