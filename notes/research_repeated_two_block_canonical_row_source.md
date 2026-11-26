# A full canonical row source for repeated two-crossing blocks

Research proof, 8 November 2026. No numerical evaluation is used.

The complete physical coefficient packet of
[the half-interval theorem](research_repeated_two_block_half_interval_packet.md)
extends to an explicitly defined canonical row interpolation on a fixed
complex neighborhood of every compact subinterval of \((0,1/2]\).
All rows revived by a noninteger index are included and bounded. This
supplies an actual holomorphic input for a subsequent two-crossing
operator, rather than merely continuing its proposed action. It does
not yet prove the coupled saddle or the full moment asymptotic for
arbitrarily many repeated blocks.

## 1. The exact symmetric kernel and all capped moments

Use \(D=N-1\), \(q=e^{\pi i/N}\),
\(S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N)\), and the full original
\(A_2=JM^2\). Define the unitary diagonal matrix
\[
 \mathsf D_{jj}=i^j q^{(j^2-j)/2},
 \qquad
 B_{ij}=\begin{cases}
 Nq^{-ij}\dfrac{S_{i+j}}{S_i^2S_j^2},&i+j\le D,\\
 0,&i+j\ge N.
 \end{cases}
 \tag{1}
\]
The original exact two-crossing coefficient formula gives
\[
 A_2=\mathsf D B\mathsf D,\qquad B^T=B,\qquad
 K_2=(M^2)^*M^2=\mathsf D^*\overline B B\mathsf D.
 \tag{2}
\]
These are identities on the full original coefficient space, not
on its quotient by ordinary root values. Since \(\mathsf D e_0=e_0\),
\[
 \mu_{m,N}=e_0^*(\overline B B)^m e_0.
 \tag{3}
\]
Starting with \(W_0=e_0\), apply \(B,\overline B,B,\overline B,\ldots\)
successively to obtain \(W_m\). Then
\[
 \mu_{m,N}=\|W_m\|_2^2,\qquad
 (W_1)_j=\frac N{S_j},\qquad
 W_2=\mathsf D K_2e_0.
 \tag{4}
\]
For even \(m=2k\), \(W_m=(\overline B B)^k e_0\);
for odd \(m=2k+1\), \(W_m=B(\overline B B)^k e_0\).
This verifies the norm identity in both cases. The original capped
scalar remains \(Z_{2,m,N}=\kappa^{2m-1}\mu_{m,N}\), with
\(\kappa=q^{D^2/2}\).

## 2. Canonical continuation includes the entire revived support

Let \(G_N\) be the original canonical sine factorial. Its exact
identities, from
[factorial continuation](research_terminal_reflected_factorials.md), are
\[
 G_N(j)=S_j\quad(0\le j\le D),\qquad
 G_N(z)G_N(D-z)=N,\qquad
 G_N(z+N)=-2\sin(\pi z)G_N(z).
 \tag{5}
\]
In particular \(G_N(k)=0\) for every integer
\(N\le k\le2N-1\). The shifts continue \(G_N\) holomorphically
through the first positive zero interval.

Define two exact kernel interpolants
\[
 \mathcal B_N^{\pm}(s,t)
   =N e^{\pm i\pi Nst}
      \frac{G_N(N(s+t))}{G_N(Ns)^2G_N(Nt)^2}.
 \tag{6}
\]
At physical \(s=i/N,t=j/N\), \(\mathcal B_N^-\) equals
\(B_{ij}\), and \(\mathcal B_N^+\) equals \(\overline{B_{ij}}\),
including every zero outside the triangle in (1).

The full second row source is
\[
 \begin{split}
 \widetilde T_N(t)&=
    \sum_{j=0}^D e^{i\pi jt}\frac{G_N(j+Nt)}{S_j^3},\\
 \widetilde W_{2,N}(t)&=
    \frac{N^2}{G_N(Nt)^2}\widetilde T_N(t).
 \end{split}
 \tag{7}
\]
It is holomorphic on every fixed complex neighborhood with
\(0<\Re t<1\) on which the numerator arguments stay short of
the next negative or positive period. Only neighborhoods of compact
subsets of \((0,1/2]\) are used here. At every physical row
\(t=n/N\), equations (5)--(7) give exactly
\[
 \widetilde W_{2,N}(n/N)=(W_2)_n
  =\frac{N^2}{S_n^2}
      \sum_{j=0}^{D-n}q^{nj}\frac{S_{j+n}}{S_j^3}.
 \tag{8}
\]
Thus no support convention is continued by fiat: the terms beyond
the physical upper limit are present in (7), and vanish at the
physical indices by the exact first-zero identity.

## 3. A zero-safe bound at and beyond the first numerator wall

We use the original primitive \(J\) and its upper and lower
continuations \(J_\pm\) across the negative real axis. On a compact
region \(0<\Re w<2\), avoiding only the two outer endpoints,
the reciprocal reflection estimate of
[uniform factorial bounds](research_uniform_factorial_and_boundary_decay.md),
Section 2, gives
\[
 |G_N(Nw)|\le C N^C e^{N\mathcal J_\#(w)},
 \qquad
 \mathcal J_\#(w)=-\Re J_{\rm side}(1-w).
 \tag{9}
\]
The real upper envelope \(\mathcal J_\#\) is continuous across
the first numerator wall \(\Re w=1\), including its real zero.
To check the finite shifts in (9), write the reflection exactly as
\[
 G_N(Nw)=\frac N{G_N(N(1-w)-1)}
       =\frac N{G_N(Nv-1/2)},\qquad
 v=1-w-\frac1{2N}.
 \tag{10}
\]
The cited reciprocal estimate applies to this full closed strip,
with both reflected exponential terms retained. Moving the primitive
argument by \(1/(2N)\) changes its real part by
\(O(\log N/N)\), uniformly even at zero: integrate the local
logarithmic singularity, or split a segment into its distance at
most \(1/N\) from zero and its complement. This accounts for
the polynomial factor in (9).

On the real line, the two values needed below are exactly
\[
 \mathcal J_\#(w)=
 \begin{cases}J(w),&0\le w\le1,\\
 J(w-1),&1\le w<2.
 \end{cases}
 \tag{11}
\]
For the second branch this uses
\(\Re J_\pm(-r)=-J(r)\). Off the real line the reflected
carrier in \(J_\pm\) is retained in (9); it is not dropped
on the grounds that the physical rows vanish.

## 4. Complete holomorphic packet on a fixed row neighborhood

Use \(x(t),\Phi(t),A(t)\) from the fully proved half-interval
packet. Fix any compact interval \(K\subset(0,1/2]\).

**Theorem 1.** There is a fixed open complex neighborhood
\(\mathcal U_K\) of \(K\), independent of \(N\), such that
\[
 \boxed{\quad
 \widetilde T_N(t)=N^{-1/2}A(t)e^{N\Phi(t)}
                         (1+O_K(N^{-1})),\qquad t\in\mathcal U_K.
 \quad}
 \tag{12}
\]
The relative error is holomorphic there. On a smaller fixed
neighborhood, every fixed derivative of the relative error is
\(O_K(N^{-1})\). Consequently
\[
 \boxed{\quad
 \widetilde W_{2,N}(t)
   =N^{1/2}\frac{A(t)}{2\sin\pi t}
       e^{N[\Phi(t)-2J(t)]}(1+O_K(N^{-1})).
 \quad}
 \tag{13}
\]

*Proof.* Use the fixed retained cuts \(a,b\) from the half-interval
theorem. The full summand of (7), with \(x=j/N\), has the uniform
zero-safe upper envelope
\[
 \mathcal E(x,t)=
   \mathcal J_\#(x+t)-3J(x)-\pi x\Im t,\qquad 0\le x\le1.
 \tag{14}
\]
The last term is the literal carrier from \(e^{i\pi jt}\).
The denominator bound is the physical endpoint-uniform factorial
estimate; the numerator is (9). Thus each summand is bounded by
a polynomial times \(e^{N\mathcal E(x,t)}\), uniformly in its
entire physical index, including zero and \(D\).

For real \(t\in K\), whenever \(x+t\le1\), the omitted
rows outside \((a,b)\) are exactly those paid by the complete
half-interval theorem. When \(x+t\ge1\), one has
\(x\ge1-t\ge1/2\) and \(0\le x+t-1\le t\le1/2\), so
\[
 \mathcal E(x,t)=J(x+t-1)-3J(x)\le0
                   <b_2/2\le\Re\Phi(t).
 \tag{15}
\]
This includes all newly revived rows and their moving zero wall.
Hence on the full compact omitted set there is one strict uniform
gap below \(\Re\Phi(t)\). The envelope (14) is continuous on
a fixed neighborhood of this set, including the first wall by (9).
Shrinking that neighborhood preserves the gap. Summing the full
omitted set therefore remains exponentially smaller than the packet
for every complex \(t\) in a fixed neighborhood of \(K\).

The retained indices and cuts are fixed. Their exact canonical
interpolant, finite cotangent rectangles, two horizontal remainders,
four vertical remainders, and both unweighted joins are the ones
already proved in the half-interval theorem. All their strict gaps
persist on a sufficiently small fixed complex neighborhood. The
critical branch is simple and remains inside the same regular
factorial charts. Analytic Gaussian expansion on this finite cover
therefore gives (12), including the original \(+N\) density and
nonzero coefficient. The retained and full sums are holomorphic;
division by the nonzero packet makes their relative error
holomorphic as well. Cauchy's estimate on smaller fixed neighborhoods
gives the derivative assertion. The ordinary regular expansion of
\(G_N(Nt)^2\) then gives (13). \(\square\)

Theorem 1 concerns this specified canonical continuation of the
actual coefficient rows. It does not identify a nonphysical row with
an ordinary colored-knot boundary value. On every physical row the
source is exactly the original one, with all normal directions and
both parities retained.

For further composition there is now an exact analytic output
formula at every step:
\[
 \widetilde W_{m+1,N}(t)=
       \sum_{j=0}^D\mathcal B_N^{\varepsilon_m}(j/N,t)(W_m)_j,
 \qquad
 \varepsilon_m=\begin{cases}+,&m\text{ odd},\\-,&m\text{ even}.
 \end{cases}
 \tag{16}
\]
It equals the next actual vector at physical rows. Formula (13)
supplies a proved holomorphic input for the first new step in (16).
A complete induction still needs the subsequent coupled critical
point, its source-valid complex domain, and all omitted-row and
contour-current estimates. Those requirements are not inferred from
the positive norm identity (4).
